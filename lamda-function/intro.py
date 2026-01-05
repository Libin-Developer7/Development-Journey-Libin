"""
lambdafunction: anonymous function with single expression

"""
add_numbers=lambda n1,n2:n1+n2
print(add_numbers(10,20))
squares=lambda n:n**2
print(squares(2))
is_negative=lambda n:True if n<0 else False
print(is_negative(-5))
is_century_year=lambda yr:True if yr%100==0 else False
print(is_century_year(2000))

employee_salary={
    "john":25000,
    "jacob":30000,
    "arun":20000,
    "dibin":40000,
    "kevin":50000
}
srt_employee=sorted(employee_salary,key=lambda k:employee_salary.get(k))
srt_employee=sorted(employee_salary,key=lambda k:employee_salary.get(k),reverse=True)
print(srt_employee)

employees=[
    ["sam",34000,4],
    ["ram",44000,3],
    ["jacob",54000,5],
    ["tahru",4000,6],
    ["jibin",74000,6],
]

srt_emp_exp=sorted(employees,key=lambda lst:lst[2])
print(srt_emp_exp)
srt_emp_salary=sorted(employees,key=lambda lst:lst[1])
print(srt_emp_salary)

