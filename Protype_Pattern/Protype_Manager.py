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
        return super(FAR, self).clone()
    
    def display(self):
        print("Feasibility Report!")


if __name__ == '__main__':
    doc = [1]
    doc1 = FAR(doc)
    doc2 = doc1.clone()
    print(id(doc1.doc) == id(doc2.doc))


