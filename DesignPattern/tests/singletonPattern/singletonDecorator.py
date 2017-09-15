def Singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@Singleton
class Test(object):
    def __init__(self):
        pass

    def test(self):
        print "hello, world"
if __name__ == '__main__':
    for i in xrange(20):
        print id(Test())
