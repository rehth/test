from redis import StrictRedis

if __name__ == '__main__':
    # 默认参数
    red = StrictRedis(host='localhost', port='6379', db=0)
    # 添加一个string类型的数据 key: name, val: zhang
    reg = red.set('name', 'zhang')
    print(reg)
    # 多获取：name
    s = red.mget('name')
    # 获取所有的变量
    k = red.keys()
    # 查询变量user的类型
    t = red.type('user')
    # 获取hash类型的数据　user
    u = red.hmget('user', 'name', 'passwd')
    print(s, k, t, u)
    # 删除redis数据库中的name
    red.delete('name')
    print(red.keys())


