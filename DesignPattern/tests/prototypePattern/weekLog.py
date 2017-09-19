# python has no absract class, we use abc to create
from abc import ABCMeta, abstractmethod


class logObject(object):
    '''abstract class'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self): pass


class weekLog(logObject):
    def __init__(self):
        self.name = ""
        self.date = ""
        self.content = ""

    def setName(self, name):
        self.name = name

    def setDate(self, date):
        self.date = date

    def setContent(self, content):
        self.content = content

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getContent(self):
        return self.content

    def clone(self):
        obj = weekLog()
        obj.setName(self.name)
        obj.setDate(self.date)
        obj.setContent(self.content)
        return obj

if __name__ == "__main__":
    obj = weekLog()
    obj.setName("zhang wuji")
    obj.setDate("2017-9-19")
    obj.setContent("work overtime!")
    print '----------------------'
    print obj.getName()
    print obj.getDate()
    print obj.getContent()
    print '----------------------'
    obj2 = obj.clone()
    obj2.setDate("2017-9-20")
    obj2.setName("zhang sanfeng")
    print obj2.getName()
    print obj2.getDate()
    print obj2.getContent()
    print '----------------------'
    obj3 = obj.clone()
    obj3.setDate("2017-9-21")
    obj3.setName('Duan yu')
    print obj3.getName()
    print obj3.getDate()
    print obj3.getContent()
    print '----------------------'
    print id(obj)
    print id(obj2)
    print id(obj3)

