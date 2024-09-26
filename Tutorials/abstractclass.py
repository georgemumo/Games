from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("Car is going")
    def stop(self):
        print("Car is stopping")
class Motorcycle(Vehicle):
    def go(self):
        print("Motorcycle is going")
    def stop(self):
        print("Motorcycle is stopping")