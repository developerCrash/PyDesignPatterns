from Observer import *


class Client:
    if __name__ == '__main__':

        w = WheatherForcasting()
        p = PhoneApp()

        w.register(p)
        w.setTemperature(30)
