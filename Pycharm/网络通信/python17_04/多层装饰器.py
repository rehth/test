def bold(func):
    def inner():
        return "<b>%s</b>" % func()
    return inner


def italic(func):
    def inner():
        return "<i>%s</i>" % func()
    return inner


@bold
@italic
def hello():
    return "hello world"

print(hello())  # <b><i>hello world</i></b>
