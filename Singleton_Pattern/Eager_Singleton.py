class EagerSingleton():
    '''
        Eager Pattern for Singleton
    '''
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(EagerSingleton, cls).__new__(cls)
        return cls.__instance        
    
    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        return EagerSingleton.__instance


test_1 = EagerSingleton()
test_2 = EagerSingleton()
print(id(test_1) == id(test_2))
