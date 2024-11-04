class PathCalculatingStrategy:
    def __init__(self):
        pass

    def calculatePath(self, src, dest):
        pass


class BikePathStrategy(PathCalculatingStrategy):
    def __init__(self):
        pass

    def calculatePath(self, src, dest):
        print("Calculating path through Bike from " + str(src) + " to " + str(dest))


class CarPathStrategy(PathCalculatingStrategy):

    def __init__(self):
        pass

    def calculatePath(self, src, dest):
        print("Calculating path through Car from " + str(src) + " to " + str(dest))


class WalkPathStrategy(PathCalculatingStrategy):

    __instance = None

    def __init__(self):
        if WalkPathStrategy.__instance != None:
            raise Exception("Walk Path Stretegy already created")
        else:
            WalkPathStrategy.__instance = self
    @staticmethod
    def getInstance(self):
        if WalkPathStrategy.__instance == None:
            WalkPathStrategy()
        return WalkPathStrategy.__instance


    def calculatePath(self, src, dest):
        print("Calculating path through Walk from " + str(src) + " to " + str(dest))

class PathCalculatingFactory():
    def __init__(self):
        pass
    def pathCalculator(self, mode):
        if mode == 'Bike':
            return BikePathStrategy()
        elif mode == 'Car':
            return CarPathStrategy()
        elif mode == 'Walk':
            return WalkPathStrategy()
