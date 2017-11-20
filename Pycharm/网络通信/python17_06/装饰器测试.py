import pymysql


def wapper(func):
    def inner():
        conn = pymysql.connect(host='localhost', port=3306, database='jing_dong', user='root',
                               password='mysql', charset='utf8')
        curs = conn.cursor()
        ret = func(curs)
        curs.close()
        conn.close()
        return ret
    return inner


@wapper
def sql_test(curs):
    curs.execute("select * from goods")
    ret = curs.fetchall()
    return ret

print(sql_test())