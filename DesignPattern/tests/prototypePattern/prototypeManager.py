import threading
lock = threading.Lock()


class officialDocument(object):

    def __init__(self):
        self.name = ""
        self.date = ""
        self.content = ""

    def display(self): pass

    def setName(self, name):
        self.name = name

    def setData(self, date):
        self.date = date

    def setContent(self, content):
        self.content = content

    def getName(self):
        return self.name

    def getData(self):
        return self.date

    def getContent(self):
        return self.content

    def clone(self):
        obj = officialDocument()
        obj.setName(self.name)
        obj.setData(self.date)
        obj.setContent(self.content)
        obj.display = self.display
        return obj


class FAR(officialDocument):
    def clone(self):
        return super(FAR, self).clone()

    def display(self):
        print "Feasibility Analysis Report"


class SRS(officialDocument):
    def clone(self):
        return super(SRS, self).clone()

    def display(self):
        print "Software Requirements Specification"


class PrototypeManager(object):
    # private static variable member
    __instance = None

    def __init__(self):
        self.hashTable = {}

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                lock.acquire()
                if not cls.__instance:
                    cls.__instance = super(PrototypeManager, cls).__new__(cls,
                                                                          *args,
                                                                          **kwargs)
            finally:
                lock.release()
        return cls.__instance

    def addOfficialDocument(self, key, doc):
        self.hashTable[key] = doc

    def getOfficialDocument(self, key):
        doc = self.hashTable.get(key)
        if doc:
            return doc.clone()
        return None


if __name__ == '__main__':
    pm = PrototypeManager()
    pm.addOfficialDocument('far', FAR())
    pm.addOfficialDocument('srs', SRS())
    obj1 = pm.getOfficialDocument('far')
    obj1.display()
    obj2 = pm.getOfficialDocument('far')
    obj2.display()
    print id(obj1)
    print id(obj2)

    obj3 = pm.getOfficialDocument('srs')
    obj3.display()
    obj4 = pm.getOfficialDocument('srs')
    obj4.display()
    print id(obj3)
    print id(obj4)
