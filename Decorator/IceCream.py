class IceCream:
    def getCost(self):
        pass

    def getDesc(self):
        pass


class Cone(IceCream):
    def __init__(self) -> None:
        pass

    def getCost(self):
        return 20

    def getDesc(self):
        return " Cone "


class VanillaScoop(IceCream):
    def __init__(self, iceCream):
        self.iceCream = iceCream

    def getCost(self):
        return self.iceCream.getCost() + 30

    def getDesc(self):
        return self.iceCream.getDesc() + " Vanilla_Scoop"


class OrangeScoop(IceCream):
    def __init__(self, iceCream):
        self.iceCream = iceCream

    def getCost(self):
        return self.iceCream.getCost() + 40

    def getDesc(self):
        return self.iceCream.getDesc() + " Orange_Scoop"


class ChocoChip(IceCream):
    def __init__(self, iceCream):
        self.iceCream = iceCream

    def getCost(self):
        return self.iceCream.getCost() + 50

    def getDesc(self):
        return self.iceCream.getDesc() + "ChocoChip"