class Singleton:

    __instance = None
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton already exists")
        else:
            Singleton.__instance = self

    @staticmethod
    def getInstance(self):
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
