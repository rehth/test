import time
import random
import re
import urllib.parse
import pymysql

url_list = list()
g_templates_path = './templates'
connection = pymysql.connect(host='localhost', user='root', password='mysql',
                                  database='stock_db', port=3306, charset='utf8')
curs = connection.cursor()


def route(path):
    def warpper(func):
        url_list.append((path, func))

        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return warpper


@route("/index.html")
def index(path):
    # 制作response_body
    # global curs
    index_html = read_file(path)
    sql = 'select * from info'
    curs.execute(sql)
    curs_info = curs.fetchall()
    html_template = """<tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>
                                <input type="button" value="添加" id="toAdd"
                                 name="toAdd" systemidvaule="%s">
                            </td>
                        </tr>
                    """
    html = ''
    for item in curs_info:
        html += html_template % (item[0], item[1], item[2], item[3], item[4],
                                 item[5], item[6], item[7], item[0])
    index_html = re.sub("\{%content%}", html, index_html)
    return index_html.encode()


@route("/center.html")
def center(path):
    center_html = read_file(path)
    sql = 'select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from ' \
          'focus as f inner join info as i on f.info_id = i.id;'
    curs.execute(sql)
    curs_info = curs.fetchall()
    # 股票代码 	股票简称 	涨跌幅 	换手率 	最新价(元) 	前期高点 	备注信息
    html_template = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                       <td>
                           <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                       </td>
                       <td>
                           <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                       </td>
                   </tr>"""
    html = ''
    for item in curs_info:
        html += html_template % (item[0], item[1], item[2], item[3], item[4],
                                 item[5], item[6], item[0], item[0])
    center_html = re.sub("\{%content%}", html, center_html)
    return center_html.encode()


# /add/4.html
@route(r'/add/(\d+)\.html')
def add(rule, path):
    add_id = re.match(rule, path).group(1)
    # print(add_id)
    curs.execute("select * from focus WHERE info_id = %s", [add_id])
    if curs.fetchone():
        return "你已经添加了该股票，请不要重复添加".encode()

    add_sql = "insert into focus(info_id) values (%s)"
    curs.execute(add_sql, [add_id])
    connection.commit()
    return '添加成功'.encode()


# /update/000036.html
@route(r"/update/(\d{6})\.html")
def update(rule, path):
    update_code = re.match(rule, path).group(1)
    # print(update_code)
    update_html = read_file('/update.html')
    # 股票名称i.short  备注信息f.note_info
    curs.execute("select i.short, f.note_info from info as i inner join focus as f "
                 "on i.id = f.info_id where i.code = %s", [update_code])
    # print(curs.fetchone())
    select_name, select_note = curs.fetchone()
    # {%code%}
    update_html = re.sub(r"\{%code%}", select_name, update_html)
    # { % note_info %}
    update_html = re.sub(r"\{%note_info%}", select_note, update_html)
    return update_html.encode()


# /update/%E6%BB%A8%E5%8C%96%E8%82%A1%E4%BB%BD/%E5%98%BB%E5%98%BB.html
@route(r"/update/(\S+)/(\S+)\.html")
def update_data(rule, path):
    ret = re.match(rule, path)
    # 股票名称 要进行　url解码　urllib.parse.unquote()
    update_short = urllib.parse.unquote(ret.group(1))
    # 股票修改后的备注
    update_note = urllib.parse.unquote(ret.group(2))

    # 股票名称i.short  备注信息f.note_info
    update_sql = "update focus set note_info = %s WHERE focus.info_id = (select id from info where info.short = %s)"
    curs.execute(update_sql, [update_note, update_short])
    # print("ret", ret)
    # 提交
    connection.commit()

    return "更新成功".encode()


def read_file(path):
    try:
        with open(g_templates_path + path) as f:
            html = f.read()
    except FileNotFoundError as e:
        return str(e)
    else:
        return html


class Application(object):
    def __init__(self, url):
        self.url_list = url
        print(self.url_list)

    def __call__(self, env, start_response):
        path = env.pop("path")
        print(path)
        head_list = list(env.items())
        for url, func in self.url_list:

            if path == url:
                start_response("200 OK", head_list)
                return func(path)

            match_url = re.match(url, path)
            if match_url:
                start_response("200 OK", head_list)
                return func(url, path)
        else:
            start_response("400 Not Found",  head_list)
            return "hello world!!!".encode()

    def __del__(self):
        curs.close()
        connection.close()
        print("关闭数据库连接")
        # pass

app = Application(url_list)
