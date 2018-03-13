# [大话设计模式Python实现-代理模式](http://www.cnblogs.com/onepiece-andy/p/python_proxy_pattern.html)  
代理模式(Proxy Pattern):为其他对象提供一种代理以控制对这个对象的访问  
```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Andy'

"""
大话设计模式
设计模式——代理模式
代理模式(Proxy Pattern):为其他对象提供一种代理以控制对这个对象的访问
实现:戴励 替 卓贾易 送礼物给 娇娇
模型:
#公共接口类
class InterFace:
    def request(self):
        pass
#真实类
class RealSubject(InterFace):
    def request(self):
        print 'RealSubject request'
#代理类 调用真实类的内部方法
class ProxySubject(InterFace)
    def request(self):
        self.real = RealSubject()
        self.real.request()
"""


# 送礼物接口
class GiveGift(object):
    # 送洋娃娃
    def GiveDolls(self):
        pass

    # 送花
    def GiveFlowers(self):
        pass

    # 送巧克力
    def GiveChocolate(self):
        pass


# 被追求者类
class SchoolGirl(object):
    def __init__(self, name):
        self.name = name


# 追求者类
class Pursuit(GiveGift):
    def __init__(self, Girl):
        self.Girl = Girl

    def GiveDolls(self):
        print self.Girl.name, '送你洋娃娃'

    def GiveFlowers(self):
        print self.Girl.name, '送你花'

    def GiveChocolate(self):
        print self.Girl.name, '送你巧克力'


# 代理类
class Proxy(GiveGift):
    def __init__(self, Girl):
        self.proxy = Pursuit(Girl)

    # 送洋娃娃
    def GiveDolls(self):
        self.proxy.GiveDolls()

    # 送花
    def GiveFlowers(self):
        self.proxy.GiveFlowers()

    # 送巧克力
    def GiveChocolate(self):
        self.proxy.GiveChocolate()


if __name__ == '__main__':
    jiaojiao = SchoolGirl('jiaojiao')
    daili = Proxy(jiaojiao)
    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()
```
上面的类的设计如下图：   
![proxy pattern](https://images2017.cnblogs.com/blog/1264910/201711/1264910-20171102111204795-1924795260.png)  
代理类Proxy引用代理的实体Pursite，提供与Pursite相同的接口来代替实体  
# Reference  
[大话设计模式Python实现-代理模式](http://www.cnblogs.com/onepiece-andy/p/python_proxy_pattern.html)  
