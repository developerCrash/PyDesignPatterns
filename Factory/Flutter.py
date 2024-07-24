from SupportedPlatform import *
from .UIFactory import *


class Flutter:
    def __init__(self, platform):
        self.platform = platform

    def setTheme(self):
        print("Setting Dark Theme")

    def createUIFac(self):
        return UIFactoryFactory.createUIFactory(self.platform)
