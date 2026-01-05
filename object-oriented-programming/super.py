class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"student name {self.name}, age {self.age}, gender {self.gender}")
class Student(Person):
    def __init__(self,name,age,gender,roll_number,course):
        super().__init__(name,age,gender)
        self.roll_number=roll_number
        self.course=course
    def display(self):
        super().display()
        print(f"Rollnumber:{self.roll_number},course:{self.course}")

student1=Student("john",27,"male",1234,"python")
student1.display()
