'''
python can't use hungry pattern, this script can't run normally.
'''
import random


class LoadBalancer(object):
    # private static variable member
    __instance = LoadBalancer()

    def __init__(self):
        self.server_list = []

    @classmethod
    def getLoadBalancer(cls):
        # python static method can not use static variable and function and
        # python static method is just like a global function
        # python class method can directly use static method
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
    c.test()
