"""
Sorry, Python doesn't support IoDH like Java~
"""
class Singleton():
    '''
    Initialization on Demand Holder
    '''
    def __init__(self):
        pass

    class __Holder():        
        __instance = Singleton()
        def __init__(self):
            pass

    @classmethod
    def getInstance(cls):
        return cls.__Holder.__instance


test1 = Singleton()
test2 = Singleton()
print(id(test1.getInstance()) == id(test2.getInstance()))