"""
contructor. Normal method. Special name class name python(__init__)
automatically invoked during object creation

"""
class Mobile:
    def __init__(self,title,price,brand,features):
        self.title=title
        self.price=price
        self.brand=brand
        self.features=features
    def display(self):
        print(f"mobile title is {self.title}. It costs {self.price}. Its featues are {self.features}")
mobile_instance1=Mobile("iphone",60000,"apple","fast processor, great camera")
mobile_instance1.display()
mobile_instance2=Mobile("pixel",50000,"google","fast processor,good camera")
mobile_instance2.display()
"""
oop features
1 inheritance
===========
mechanism of child class accessing parent class attributes and methods
1 single inheritance
2 multilevel inheritance
3 multiple inheritance

2 polymorphism
many forms (more than one form) eg: int() with strings and integers
1 method overloading
2 method overriding

3 abstraction
hiding implimentation details
"""