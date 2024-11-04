
class GMap:
    def __init__(self):
        pass
    def calulateMap(self, src, dest, mode):
        p = PathCalculatingFactory().pathCalculator(mode)
        p.calculatePath(src, dest)
