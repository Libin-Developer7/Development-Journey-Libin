class GrandParent:
    def properties(self):
        print("land and vintage home")
class Parent(GrandParent):
    def vehicle(self):
        print("polo car")
class Child(Parent):
    def gadgets(self):
        print("iphone","ipad","laptop")
child_instance1=Child()
child_instance1.gadgets()
child_instance1.vehicle()
child_instance1.properties()

class Course:
    def __init__(self,course_name):
        self.course_name=course_name
    def display(self):
        print(self.course_name)
class Module(Course):
    def __init__(self,course_name,module_name):
        super().__init__(course_name)
        self.module_name=module_name
    def display(self):
        super().display()
        print(self.module_name)
class Lesson(Module):
    def __init__(self, course_name, module_name,lesson_name):
        super().__init__(course_name, module_name)
        self.lesson_name=lesson_name
    def display(self):
        super().display()
        print(self.lesson_name)

lesson_instance1=Lesson("python","OOPS","constructor")
lesson_instance1.display()
lesson_instance2=Lesson("python","OOPS","inheritance")
lesson_instance2.display()
        