class Lazy_Singleton():
    __instance = None
    def __init__(self):
        if Lazy_Singleton.__instance == None:
            print('class has not been instatialized!')
        else:
            print('class has been instatialized!')

    @classmethod
    def getInstance(cls):
        if cls.__instance == None:
            cls.__instance = Lazy_Singleton()
        return cls.__instance
    
test1 = Lazy_Singleton()
test1.getInstance()
test2 = Lazy_Singleton()