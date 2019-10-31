class TaskManager():
    __tm = None
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if TaskManager.__tm == None:
            TaskManager.__tm = TaskManager()
        return TaskManager.__tm

test1 = TaskManager().get_instance()
test2 = TaskManager().get_instance()
print(test1._TaskManager__tm)
print(test2._TaskManager__tm)