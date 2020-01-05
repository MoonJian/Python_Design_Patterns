from abc import abstractmethod

class AbstractFile():
    @abstractmethod
    def add(self, file):
        pass

    @abstractmethod
    def remove(self, file):
        pass

    @abstractmethod
    def getChild(self, i):
        pass

    @abstractmethod
    def killVirus(self):
        pass


class ImageFile(AbstractFile):
    def __init__(self, name):
        self.name = name

    def add(self, file):
        print("Not Supporting!")

    def remove(self, file):
        print("Not Supporting!")        

    def getChild(self, i):
        print("Not Supporting!")        

    def killVirus(self):
        print("----killing image file virus: {}".format(self.name))

class TextFile(AbstractFile):
    def __init__(self, name):
        self.name = name

    def add(self, file):
        print("Not Supporting!")

    def remove(self, file):
        print("Not Supporting!")        

    def getChild(self, i):
        print("Not Supporting!")        

    def killVirus(self):
        print("----killing text file virus: {}".format(self.name))

class VideoFile(AbstractFile):
    def __init__(self, name):
        self.name = name

    def add(self, file):
        print("Not Supporting!")

    def remove(self, file):
        print("Not Supporting!")        

    def getChild(self, i):
        print("Not Supporting!")        

    def killVirus(self):
        print("----killing video file virus: {}".format(self.name))

class Folder(AbstractFile):
    def __init__(self, name):
        self.fileList = []
        self.name = name

    def add(self, file):
        self.fileList.append(file)        

    def remove(self, file):
        self.fileList.remove(file)
    
    def getChild(self, i):
        return self.fileList[i]

    def killVirus(self):
        print("****killing folder file virus: {}".format(self.name))
        for f in self.fileList:
            f.killVirus()


if __name__ == "__main__":
    folder1 = Folder("Sunny's file")
    folder2 = Folder("Image File")                
    folder3 = Folder("Text File")
    folder4 = Folder("Video FIle")

    file1 = ImageFile("1.jpg")
    file2 = ImageFile("2.gif")
    file3 = TextFile("3.txt")
    file4 = TextFile("4.doc")
    file5 = VideoFile("5.rmvb")

    folder2.add(file1)
    folder2.add(file2)
    folder3.add(file3)
    folder3.add(file4)
    folder4.add(file5)
    folder1.add(folder2)
    folder1.add(folder3)
    folder1.add(folder4)

    folder1.killVirus()