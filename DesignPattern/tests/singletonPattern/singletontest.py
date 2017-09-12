# -*- coding: utf-8 -*-
import threading
import time
'''
reference: https://www.bbsmax.com/A/6pdDvlDyJw/
'''


class Singleton(object):

    # 定义静态变量实例
    __singleton = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if Singleton.__singleton is None:
            Singleton.__singleton = Singleton()
        return Singleton.__singleton


def test_singleton_in_thread():
    global ret
    time.sleep(1)
    if not ret:
        ret = id(Singleton.get_instance())
    else:
        if ret != id(Singleton.get_instance()):
            print ret, id(Singleton.get_instance())

if __name__ == "__main__":
    idx = 0
    ret = None
    while 1:
        threading.Thread(target=test_singleton_in_thread).start()
        # idx += 1
        # if idx > 0X1000:
        #     break
