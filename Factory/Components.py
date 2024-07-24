class Button:
    def __init__(self):
        pass
    def click(self):
        print("Button is clicked")


class Scroll:
    def __init__(self):
        pass

    def horizantalScroll(self):
        print("Scrolling Horizantally")

    def verticalScroll(self):
        print("Scrolling Vertically")

class DropDown:
    def __init__(self):
       pass
    def select(self):
        print("Select an item in the dropdown")


class AndroidButton(Button):
    def __init__(self):
        print("Creating an Android Button")


class AndroidScroll(Scroll):
    def __init__(self):
        print("Creating an Android Scroll")


class AndroidDropDown(DropDown):
    def __init__(self):
        print("Creating an Android DropDown")


class IOSButton(Button):

    def __init__(self):
        print("Creating an IOS Button")


class IOSScroll(Scroll):
    def __init__(self):
        print("Creating an IOS Scroll")


class IOSDropDown(DropDown):
    def __init__(self):
        print("Creating an IOS DropDown")



