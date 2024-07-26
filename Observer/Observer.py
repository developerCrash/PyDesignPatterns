class Observer:
    def update(self, observable, *args, **kwargs):
        pass
class Observable:
    def __init__(self):
        self.observers = []

    def register(self, Observable):
        self.observers.append(Observable)

    def deregister(self, Observable):
        self.observers.pop(Observable)
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)


class WheatherForcasting(Observable):
    def setTemperature(self, temperature):
        self.temperature = temperature
        self.notify()


class PhoneApp(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WheatherForcasting):
            temperature = observable.temperature
            print("This is  the temperature as denoted " + str(temperature))

