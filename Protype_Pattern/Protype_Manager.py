from abc import abstractmethod
from copy import deepcopy

class OfficialDocument():
    def __init__(self, doc=None):
        self.doc = doc

    def clone(self):
        # return OfficialDocument(self.doc) # shallow copy!
        return deepcopy(OfficialDocument(self.doc))        

    @abstractmethod
    def display(self):
        pass


class FAR(OfficialDocument):
    def __init__(self, doc=None):
        super(FAR, self).__init__(doc)

    def clone(self):
        return deepcopy(FAR(self.doc))
        # return super(FAR, self).clone()
    
    def display(self):
        print("Feasibility Report!")


class SRS(OfficialDocument):
    def __init__(self, doc=None):
        super(SRS, self).__init__(doc)

    def clone(self):
        return deepcopy(SRS(self.doc))
        # return super(SRS, self).clone()
    
    def display(self):
        print("Software Requirements Document!")        


class Protype_Manager():
    __pm = None
    __initflag = False
    def __new__(cls):
        if cls.__pm == None:
            cls.__pm = super(Protype_Manager, cls).__new__(cls)
        return cls.__pm

    def __init__(self):
        # The best way is to let it become a static attribute! Singleton uses __init__ as less as possible
        if Protype_Manager.__initflag == False:
            self.ht = {}
            self.ht['far'] = FAR()
            self.ht['srs'] = SRS()
            Protype_Manager.__initflag = True            

    def addOfficialDocument(self, key, doc):
        self.ht[key] = doc

    def getOfficialDocument(self, key):
        return self.ht[key].clone()

    @staticmethod
    def getProtypeManager():
        return Protype_Manager.__pm


if __name__ == '__main__':
    # doc = [1]
    # doc1 = FAR(doc)
    # doc2 = doc1.clone()
    # print(id(doc1.doc) == id(doc2.doc))

    pm1 = Protype_Manager().getProtypeManager()
    pm2 = Protype_Manager().getProtypeManager()
    print(id(pm1) == id(pm2))

    doc1 = pm1.getOfficialDocument('far')
    doc1.display()
    doc2 = pm1.getOfficialDocument('srs')
    doc2.display()
    print(doc1 is doc2)

    doc3 = pm2.getOfficialDocument('srs')
    doc3.display()
    doc4 = pm2.getOfficialDocument('srs')
    doc4.display()
    print(doc3 is doc4)
