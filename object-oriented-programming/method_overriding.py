class Vehicle:
    def __init__(self,brand,title):
        self.brand=brand
        self.title=title
    def move(self):
        print(self.title,"is moving")
class Car(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)
class Ship(Vehicle):
    def __init__(self, brand, title):
        super().__init__(brand, title)
    def move(self):
        print(self.title,"is sailing")
car_instance=Car("toyota","fortuner")
car_instance.move()
ship_instance=Ship("mistu","titanic")
ship_instance.move()     # here Ship child class changed the behaviour of move() method of Vehicle parent class
                        # this is called method overriding

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(self.name,"sound")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print(self.name,"bark")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print(self.name,"meow")
dog_inst=Dog("ceaser")
dog_inst.sound()
cat_inst=Cat("Kitty")
cat_inst.sound()