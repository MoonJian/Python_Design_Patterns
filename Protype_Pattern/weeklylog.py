'''
# https://stackoverflow.com/questions/48338847/how-to-copy-a-class-instance-in-python
import copy
def object_copy(instance, init_args=None):
    if init_args:
        new_obj = instance.__class__(**init_args)
    else:
        new_obj = instance.__class__()
    if hasattr(instance, '__dict__'):
        for k in instance.__dict__ :
            try:
                attr_copy = copy.deepcopy(getattr(instance, k))
            except Exception as e:
                attr_copy = object_copy(getattr(instance, k))
            setattr(new_obj, k, attr_copy)

        new_attrs = list(new_obj.__dict__.keys())
        for k in new_attrs:
            if not hasattr(instance, k):
                delattr(new_obj, k)
        return new_obj
    else:
        return instance
'''

class WeeklyLog():
    def __init__(self, name=None, date=None, content=None):
        self._name = name
        self._date = date
        self._content = content

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value

    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, value):
        self._content = value

    def clone(self):
        return WeeklyLog(self._name, self._date, self._content)


if __name__ == "__main__":
    log_previous = WeeklyLog()
    log_previous.name = "Wuji Zhang"
    log_previous.date = "Week 12"
    log_previous.content = "It's too busy this week, worked overtime everyday!"

    print("****Week Log****")
    print(log_previous.date)
    print("Name: ", log_previous.name)
    print("Content: ", log_previous.content)
    print("="*60)

    # log_new = object_copy(log_previous)
    log_new = log_previous.clone()
    log_new.date = "Week 13"
    print("****Week Log****")
    print(log_new.date)
    print("Name: ", log_new.name)
    print("Content: ", log_new.content)
    print("="*60)    

    print(log_new == log_previous)