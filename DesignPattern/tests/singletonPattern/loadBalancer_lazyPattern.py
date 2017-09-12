import random
import threading
lock = threading.Lock()


class LoadBalancer(object):
    # private static variable member
    __instance = None

    def __init__(self):
        self.server_list = []

    def __new__(cls, *args, **kwargs):
        # this function will run when create object and __init_ funtion run
        # after create object. If we don't rewrite the function, this class
        # init self will not the same with classmethod getLoadBalancer
        if not cls.__instance:
            try:
                lock.acquire()
                # double check to make sure thread safe
                if not cls.__instance:
                    cls.__instance = super(LoadBalancer, cls).__new__(cls,
                                                                      *args,
                                                                      **kwargs)
            finally:
                lock.release()
        return cls.__instance

    @classmethod
    def getLoadBalancer(cls):
        # python static method can not use static variable and function and
        # python static method is just like a global function
        # python class method can directly use static method
        # if not cls.__instance:
        #     cls.__instance = LoadBalancer()
        return cls.__instance

    # add server
    def addServer(self, serverip):
        self.server_list.append(serverip)

    # delete server
    def delServer(self, serverip):
        if serverip in self.server_list:
            self.server_list.remove(serverip)

    # get server
    def getServer(self):
        serverLen = len(self.server_list)
        if serverLen:
            i = random.randint(0, serverLen-1)
            return self.server_list[i]
        return None


class Client(object):
    def test_singleton_in_thread(self, Singleton):
        print id(Singleton.getLoadBalancer())

    def test(self):
        b1 = LoadBalancer().getLoadBalancer()
        b2 = LoadBalancer().getLoadBalancer()
        b3 = LoadBalancer().getLoadBalancer()
        if b1 == b2 and b2 == b3 and b1 == b3:
            print 'singleton pattern'
        b1.addServer("server 1")
        b1.addServer("server 2")
        b1.addServer("server 3")
        b1.addServer("server 4")
        for i in range(10):
            server = b2.getServer()
            print 'get server: ' + server

if __name__ == '__main__':
    c = Client()
    # test loadbalance
    c.test()
    # python don't have private construct function, so it can't stop the class
    # create object
    print id(LoadBalancer())
    idx = 0
    for i in xrange(10):
        threading.Thread(target=c.test_singleton_in_thread, name=None,
                         args=(LoadBalancer,)).start()
