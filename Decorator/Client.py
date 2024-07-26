from Decorator.IceCream import *


class Client:
    if __name__ == '__main__':
        ice = OrangeScoop(VanillaScoop(ChocoChip(Cone())))
        print(ice.getDesc())
