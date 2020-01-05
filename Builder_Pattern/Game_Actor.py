from abc import abstractmethod

class Actor():
    def __init__(self):
        self._type = None
        self._sex = None ### Can be improved, gender!!!
        self._face = None
        self._costume = None
        self._hairstyle = None

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        self._type = value

    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, value):
        self._sex = value    

    @property
    def face(self):
        return self._face
    @face.setter
    def face(self, value):
        self._face = value        

    @property
    def costume(self):
        return self._costume
    @costume.setter
    def costume(self, value):
        self._costume = value        

    @property
    def hairstyle(self):
        return self._hairstyle
    @hairstyle.setter
    def hairstyle(self, value):
        self._hairstyle = value        


class ActorBuilder():
    __actor = Actor()
    @abstractmethod
    def buildType(self):
        pass

    def buildSex(self):
        pass