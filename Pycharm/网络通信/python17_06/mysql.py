# from pymysql import *
import pymysql


def create_connect():
    # host = None, user = None, password = "",database = None,
    # port = 0, unix_socket = None,charset = '',
    # 建立与数据库的连接: 调用 pymysql.connect()
    conn = pymysql.connect(host='localhost', user='root', password='mysql',
                           database='jing_dong', port=3306, charset='utf8'
                           )
    # close()关闭连接  commit()提交
    # cursor()返回Cursor对象，用于执行sql语句并获得结果

    # 获取Cursor对象,用于执行sql语句：调用Connection对象的cursor()方法
    # execute(operation [, parameters ])执行语句,返回受影响的行数
    # fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
    # fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
    # close()关闭
    cur = conn.cursor()
    return conn, cur


def insert_into(name):
    conn, cur = create_connect()
    sql = "insert into goods_cates(name) values (%s)"
    ret = cur.execute(sql, [name])
    print(ret)
    # 对数据表进行更新时要    commit
    conn.commit()
    # print(ret)
    # print(cur.fetchone())
    cur.close()
    conn.close()


def update():
    pass


def delete_from():
    pass


def select(id_str=1):
    conn, cur = create_connect()
    sql = "select * from goods_cates WHERE id = %s"
    ret = cur.execute(sql, [id_str])
    print(ret)
    # conn.commit()
    # print(ret)
    # print(cur.fetchone())
    print(cur.fetchone())
    cur.close()
    conn.close()


def main():
    # insert_into('cents')
    select(2)
if __name__ == '__main__':
    main()