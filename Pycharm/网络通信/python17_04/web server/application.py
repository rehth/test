import time
import random
url_list = list()


def route(path):
    def warpper(func):
        url_list.append((path, func))

        def inner():
            return func()
        return inner
    return warpper


@route("/gettime.py")
def gettime():
    response_body = """
        <!DOCTYPE html>
        <html>
        <head>
	        <meta charset="utf-8">
	        <title>my html</title>
        </head>
        <body>
        <p>欢迎进入到我的世界！</p>
        <p>当前时间：%s</p>
        <p>当前温度：%s</p>
        <img src="./003.jpg">
        </body>
        </html>
    """ % (time.ctime(), random.randint(10, 22))
    return response_body.encode()


class Application(object):
    def __init__(self, url):
        self.url_list = url

    # env = {"Host": "%s:%s" % (client_id[0], client_id[1]), "path": path}
    def __call__(self, env, start_response):
        path = env.pop("path")
        for url,func in self.url_list:
            if path == url:
                start_response("200 OK", self.deal_env(env))
                return func()
        else:
            start_response("400 Not Found", self.deal_env(env))
            return "hello world from WSGI".encode()

    def deal_env(self, env):
        head_list = list()
        for head in env.items():
            head_list.append(head)
        return head_list

# url_list = [
#     # ("/gettime.py", gettime)
#
# ]
app = Application(url_list)
