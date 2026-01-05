from abc import ABC
from abc import abstractmethod
class Car(ABC):
    @abstractmethod
    def car_start(self):
        pass
    @abstractmethod
    def car_accelerate(self):
        pass
    @abstractmethod
    def car_stop(self):
        pass
class Fortuner(Car):
    def car_start(self):
        print("fortuner starts")
    def car_accelerate(self):
        print("fortuner accelerate")
    def car_stop(self):
        print("fortuner stops")

