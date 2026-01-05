# oops:bringing real world objects using class and objects
# class: template, design , plan for creating object, contains attributes and methods
# object:real world entity
class Car:
    name:str
    brand:str
    color:str
    seat:int
    def set_car(self,name,brand,color,seat):
        self.name=name          # self represents current object
        self.brand=brand
        self.color=color
        self.seat=seat
    def display(self):
        print("car name",self.name)
        print("car brand",self.brand)
        print("car color",self.color)
        print("car seat",self.seat)

car_instance1=Car()
car_instance1.set_car("swift","maruti","red","4")
car_instance1.display()
car_instance2=Car()
car_instance2.set_car("fortuner","toyota","white","7")
car_instance2.display()