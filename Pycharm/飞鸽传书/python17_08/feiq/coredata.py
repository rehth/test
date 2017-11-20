# 存储一些全局变量
import time

# 飞秋的广播ip
fq_broadcast = "255.255.255.255"

# 飞秋的绑定端口
fq_port = 2425

# 飞秋的版本号
fq_version = 1

# 飞秋的包编号
fq_package = int(time.time())

# 飞秋的用户名
fq_user = "user"

# 飞秋的主机名
fq_host = "pc"

# 飞秋的命令集
# 上线
IPMSG_BR_ENTRY = 0x00000001
# 下线
IPMSG_BR_EXIT = 0x00000002
# 发送消息
IPMSG_SENDMSG = 0x00000020
# 告诉我，也在线
IPMSG_ANSENTRY = 0x00000003
# 告知对方我收到了
IPMSG_RECVMSG = 0x00000021
# 文件消息
IPMSG_FILEATTACHOPT = 0x00200000
# 普通文件
IPMSG_FILE_REGULAR = 0x00000001

# udp socket
udp_socket = None

# 用户在线列表
user_list = list()

# queue 用作进程间通信
queue = None