import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download_image(image_url, image_name):
    # 打开网络地址
    response = urllib.request.urlopen(image_url)
    print(gevent.getcurrent())
    # 获取数据
    image_data = response.read()
    # 写入文件
    with open(image_name, "wb") as file:
        file.write(image_data)

if __name__ == '__main__':
    url1 = "http://ntlias-stu.boxuegu.com/favicon.ico"
    # url2 = 2
    # url3 = 3
    # 开启协程，并等待执行完成
    gevent.joinall([gevent.spawn(download_image, url1, "1.jpg")])
                    # gevent.spawn(download_image, url2, "2.jpg"),
                    # gevent.spawn(download_image, url3, "3.jpg")])