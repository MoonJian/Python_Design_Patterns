from abc import abstractmethod

class Button():
    @abstractmethod
    def display(self):
        pass

class SpringButton(Button):
    def display(self):
        print("Show shallow green button!")

class SummerButton(Button):
    def display(self):
        print("Show shallow blue button!")

class TextField():
    @abstractmethod
    def display(self):
        pass

class SpringTextField(TextField):
    def display(self):
        print("Show shallow green text field!")

class SummerTextField(TextField):
    def display(self):
        print("Show shallow blue text field!")

class ComboBox():
    @abstractmethod
    def display(self):
        pass

class SpringComboBox(ComboBox):
    def display(self):
        print("Show shallow green combobox!")

class SummerComboBox(ComboBox):
    def display(self):
        print("Show shallow blue combobox!")


class SkinFactory():
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createTextField(self):
        pass

    @abstractmethod
    def createComboBox(self):
        pass

class SpringSkinFactory(SkinFactory):
    def createButton(self):
        return SpringButton()

    def createTextField(self):
        return SpringTextField()

    def createComboBox(self):
        return SpringComboBox()

class SummerSkinFactory(SkinFactory):
    def createButton(self):
        return SummerButton()

    def createTextField(self):
        return SummerTextField()

    def createComboBox(self):
        return SummerComboBox()


if __name__ == "__main__":
    factory = SpringSkinFactory()
    factory.createButton().display()
    factory.createTextField().display()
    factory.createComboBox().display()
