from rediscluster import StrictRedisCluster

if __name__ == '__main__':
    # 构建所有的节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
    startup_nodes = [
        {'host': '192.168.93.200', 'port': '7000'},
        {'host': '192.168.93.200', 'port': '7001'},
        {'host': '192.168.93.200', 'port': '7001'},
    ]
    # 构建StrictRedisCluster对象
    src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    # 测试
    src.set('age', '18')
    info = src.mget('name', 'age')
    print(info)