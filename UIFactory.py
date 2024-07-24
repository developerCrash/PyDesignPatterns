from . import Components
from .Components import *
from .SupportedPlatform import SupportedPlatform


class UIFactory:
    def __init__(self):
        pass

    def createButton(self):
        pass

    def createScroll(self):
        pass

    def createDropDown(self):
        pass


class AndroidUIFactory(UIFactory):
    def __init__(self):
        pass

    def createButton(self):
        return AndroidButton()

    def createScroll(self):
        return AndroidScroll()

    def createDropDown(self):
        return AndroidDropDown()


class IOSUIFactory(UIFactory):
    def __init__(self):
        pass

    def createButton(self):
        return IOSButton()

    def createScroll(self):
        return IOSScroll()

    def createDropDown(self):
        return IOSDropDown()


class UIFactoryFactory():
    @staticmethod
    def createUIFactory(platform):
        if platform == "ANDROID":
            return AndroidUIFactory()
        elif platform == "IOS":
            return IOSUIFactory()



