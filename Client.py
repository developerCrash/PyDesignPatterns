from Factory.Flutter import *
from SupportedPlatform import *


class Client:
    if __name__ == '__main__':
        f = Flutter("IOS")
        ui = f.createUIFac()
        button = ui.createButton()
        scroll = ui.createScroll()
        dropdown = ui.createDropDown()



