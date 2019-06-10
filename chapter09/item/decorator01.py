import time, functools


def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s' % (func.__name__))
            print('%s %s %s()' % (time.asctime(time.localtime()), text, func.__name__))
            fc = func(*args, **kw)
            print('end call %s' % (func.__name__))
            return fc

        return wrapper

    return decorator


@log('execute')
def test1():
    print('test1 calling')


@log()
def test2():
    print('test2 calling')


test1()
test2()
