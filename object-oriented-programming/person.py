class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def get_age(self):
        print(self.age)
    @property         # decorator, a function with a feature
    def get_name(self):
        print(self.name)
person_inst=Person("jack",26,"male")
print(person_inst.gender)
person_inst.get_age()
person_inst.get_name # no brackets since property is used