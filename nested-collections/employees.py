# add 5 employee details as list of dictionary
# each employee had id,name,email,salary,department
data=[
    {"id":1122,"name":"kevin","email":"kevin@gmail.com","salary":25000,"department":"hr"},
    {"id":4342,"name":"jino","email":"jino@gmail.com","salary":30000,"department":"sales"},
    {"id":5678,"name":"johnson","email":"johnson@gmail.com","salary":35000,"department":"hr"},
    {"id":2828,"name":"john","email":"johndoe@gmail.com","salary":45000,"department":"sales"},
    {"id":1818,"name":"jacob","email":"jacob@gmail.com","salary":20000,"department":"sales"},
]
for emp in data:
    print(emp.get("name"))
all_employees=[ emp.get("name") for emp in data]
print(all_employees)
all_departments={emp.get("department") for emp in data}
print(all_departments)
sales_department={emp.get("name") for emp in data if emp.get("department")=="hr"}
print(sales_department)
salary={ emp.get("name") for emp in data if emp.get("salary")>30000}
print(salary)
dept_count={}
for emp in data:
    dept=emp.get("department")
    if dept in dept_count:
        dept_count[dept]+=1
    else:
        dept_count[dept]=1
print(dept_count)