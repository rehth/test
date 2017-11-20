import time


def app(env, start_response):
    request_path = env.pop("path")
    status = "200 OK"
    # heads = env
    response_head = start_response(status, env)
    response_body = ("hello world>>%s\r\n>>%s" % (request_path, time.ctime())).encode()
    return response_head, response_body
