#coding:utf-8
# python has no absract class, we use abc to create
from abc import ABCMeta, abstractmethod
'''
练习
Sunny软件公司欲开发了一个数据加密模块，可以对字符串进行加密。最简单的加密算法通
过对字母进行移位来实现，同时还提供了稍复杂的逆向输出加密，还提供了更为高级的求模
加密。用户先使用最简单的加密算法对字符串进行加密，如果觉得还不够可以对加密之后的
结果使用其他加密算法进行二次加密，当然也可以进行第三次加密。试使用装饰模式设计
该多重加密系统。

遵从原则：只有一个具体构件类，那么抽象装饰类可以作为该具体构件类的直接子类, 在
定义抽象装饰类的时候直接继承具体构建类，详见如下code
'''


class Data(object):
    def __init__(self, alpha):
        self.alpha = alpha

    def crypt(self):
        pass


class dataDecorator(Data):
    '''abstract class'''
    __metaclass__ = ABCMeta
    '''
    遵从原则：只有一个具体构件类，那么抽象装饰类可以作为该具体构件类的直接子类,
    在定义抽象装饰类的时候直接继承具体构建类
    '''

    @abstractmethod
    def crypt(self):
        pass

class alphabeticShiftDecorator(dataDecorator):

    def __init__(self, data):
        self.data = data
        self.alpha = data.alpha

    def crypt(self):
        self.alphaShiftCrypt()

    def alphaShiftCrypt(self):
        # print 'alphabetic shift crypt:%r' % self.data.alpha
        self.alpha = '\nalphabetic shift crypt:%r' % self.alpha


class reverseOutputDecorator(dataDecorator):

    def __init__(self, data):
        self.data = data
        self.alpha = data.alpha

    def crypt(self):
        self.reverseOutPutCrypt()

    def reverseOutPutCrypt(self):
        # print 'reverse output crypt:%r' % self.data.alpha
        self.alpha = '\nreverse output crypt:%r' % self.alpha


class modeCryptDecorator(dataDecorator):
    def __init__(self, data):
        self.data = data
        self.alpha = data.alpha

    def crypt(self):
        self.modeCrypt()

    def modeCrypt(self):
        # print 'mode crypt:%r' % self.data.alpha
        self.alpha = '\nmode crypt:%r' % self.alpha

if __name__ == '__main__':
    data = Data("fanghaiqun")
    print '------------------------------------'
    alphaCrypt = alphabeticShiftDecorator(data)
    alphaCrypt.crypt()
    print alphaCrypt.alpha
    print '------------------------------------'
    reverseCrypt = reverseOutputDecorator(alphaCrypt)
    reverseCrypt.crypt()
    print reverseCrypt.alpha
    print '------------------------------------'
    modeCrypt = modeCryptDecorator(reverseCrypt)
    modeCrypt.crypt()
    print modeCrypt.alpha
    print '------------------------------------'
    modeCrypt = modeCryptDecorator(modeCrypt)
    modeCrypt.crypt()
    print modeCrypt.alpha

