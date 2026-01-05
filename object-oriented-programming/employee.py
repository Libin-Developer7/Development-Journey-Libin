class Employee:
    def __init__(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary
    def display(self):
        print(f"employee id {self.id}, department {self.department}, salary {self.salary}")
class Developer(Employee):
    def __init__(self,id,department,salary,program,framework):
        super().__init__(id,department,salary)
        self.program=program
        self.framework=framework
    def display(self):
        super().display()                   
        print(self.program,self.framework)

dev_instance1=Developer(1234,"hr",20000,"python","mvt")
dev_instance1.display()