import pymysql
# python 的加密模块
import hashlib
import time


# 模拟京东购物与商品浏览
class JD(object):
    # 1. 建立与数据库的连接
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, database='jing_dong', user='root',
                                    password='mysql', charset='utf8')
        self.curs = self.conn.cursor()
        self.user_id = None
        self.user = None

    def show_goods(self):
        # id | name | cate_id | brand_id | price
        sql = "select g.id,g.name,c.name,b.name,g.price from goods as g inner join " \
              "goods_cates as c on g.cate_id = c.id inner join goods_brands as b on g.brand_id = b.id"
        self.curs.execute(sql)
        goods_info = self.curs.fetchall()
        for info in goods_info:
            print(info)

    def add_user(self):
        name = input("用户名")
        show_sql = "select name from customer"
        self.curs.execute(show_sql)
        for user in self.curs.fetchall():
            if user == name:
                print("用户名已存在，请重新输入")
                return
        else:
            pwd = input("密码")
            sha1_pwd = hashlib.sha1(pwd.encode()).hexdigest()
            # print(sha1_pwd)  123 --->  40bd001563085fc35165329ea1ff5c5ecbdbbeef
            sql = "insert into customer(name, pw) values (%s, %s)"
            self.curs.execute(sql, [name, sha1_pwd])
            self.conn.commit()
            insert_id = self.curs.lastrowid     # 该属性为 id
            # print(insert_id)
            if insert_id:
                print("注册成功：id 为%s, 用户名为%s" % (insert_id, name))

    def order_goods(self):
        if not self.user:
            print("请登录后再进行购物")
            return
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(date_time)    2017-10-13 23:06:56
        self.show_goods()
        try:
            num = int(input("请输入产品的序号: "))
        except Exception:
            print("输入的序号有误，请重新输入")
            return
        else:
            self.curs.execute("select id, name from goods")
            goods_id_list = self.curs.fetchall()
            # print(goods_id_list)
            for goods_id, name in goods_id_list:
                # print(type(goods_id))
                if num == goods_id:
                    # 更新订单表
                    order_sql = "insert into orders values (0, %s, %s)"
                    self.curs.execute(order_sql, [date_time, self.user_id])
                    order_id = self.curs.lastrowid
                    # 更新订单详情表
                    sql = "insert into order_detail values (0, %s, %s, 1)"
                    self.curs.execute(sql, [order_id, num])
                    # 提交数据库
                    self.conn.commit()
                    print("%s 你成功预定了商品: %s" % (self.user, name))
                    break
            else:
                print("输入的序号有误，请重新输入")

    def log_in(self):
        name = input("用户名")
        pwd = input("密码")
        show_sql = "select * from customer"
        self.curs.execute(show_sql)
        for user_id, user, passwd in self.curs.fetchall():
            if user == name and hashlib.sha1(pwd.encode()).hexdigest() == passwd:
                print(">>>>登录成功<<<<")
                self.user_id = user_id
                self.user = user
                break
        else:
            print("用户名或密码错误，请重新输入")

    def shop_basket(self):
        # 购物篮：订单号o.id　商品名c.name　订单时间o.order_date_time　价格g.price　数量d.quantity
        pass

    def __del__(self):
        self.curs.close()
        self.conn.close()


def show_menu():
    # 显示功能菜单
    print("1. 商品信息")
    print("2. 购买")
    print("3. 注册")
    print("4. 登陆")
    print("5. 购物篮")
    print("6. 退出")
    return input("请输入序号:")


def main():
    jd = JD()
    while True:
        num = show_menu()
        print(num)
        if num == "1":
            jd.show_goods()
        elif num == "2":
            jd.order_goods()
        elif num == "3":
            jd.add_user()
        elif num == "4":
            jd.log_in()
        elif num == "5":
            pass
        elif num == "6":
            print("欢迎下次使用")
            break
        else:
            print("输入错误")

if __name__ == '__main__':
    main()