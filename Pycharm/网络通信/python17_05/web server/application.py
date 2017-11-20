import time
import random
import re
import urllib.parse

url_list = list()


def route(path):
    def warpper(func):
        url_list.append((path, func))
        # user = None

        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return warpper


@route("/gettime.py\??(user=)?([^& #]*)")
def gettime(user):
    response_body = """
        <!DOCTYPE html>
        <html>
        <head>
	        <meta charset="utf-8">
	        <title>my html</title>
        </head>
        <body>
        <p>欢迎进入到我的世界！%s</p>
        <p>当前时间：%s</p>
        <p>当前温度：%s</p>
        <img src="./003.jpg">
        </body>
        </html>
    """ % (user, time.ctime(), random.randint(10, 22))
    return response_body.encode()


class Application(object):
    def __init__(self, url):
        self.url_list = url
        # print(self.url_list)

    # env = {"Host": "%s:%s" % (client_id[0], client_id[1]), "path": path}
    # /index.html?user=python
    def __call__(self, env, start_response):
        path = env.pop("path")
        head_list = list(env.items())
        for url, func in self.url_list:
            # print(path)
            match_url = re.match(url, path)
            # %E5%BC%A0
            # print(match_url.group())    # match='/gettime.py?user=python'
            if match_url:
                start_response("200 OK", head_list)
                return func(urllib.parse.unquote(match_url.group(2)))
        else:
            start_response("400 Not Found",  head_list)
            return "hello world from WSGI".encode()

# url_list = [
#     # ("/gettime.py", gettime)
#
# ]
app = Application(url_list)
