import threading

class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls in cls.objs:
            return cls.objs[cls]['obj']

        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs[cls]['obj']
            obj = object.__new__(cls)
            cls.objs[cls] = {"obj" : obj, "init" : False}
            setattr(cls, "__init__" , cls.decorate_init(cls.__init__))
            return cls.objs[cls]["obj"]
        finally:
            cls.objs_locker.release()

    @classmethod
    def decorate_init(cls, fn):
        def init_wrap(*args, **kwargs):
            if not cls.objs[cls]["init"]:
                fn(*args, **kwargs)
                cls.objs[cls]["init"] = True
            return
        return init_wrap

    def __reconfig__(self):
        pass

    def __del__(self):
        Singleton.objs.clear()
