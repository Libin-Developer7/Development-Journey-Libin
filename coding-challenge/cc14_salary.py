def teacher_salary():
    name = input("enter teacher name ")
    periods_taught = int(input("enter no. of periods taught "))
    rate_per_period = int(input("enter rate per period "))
    if periods_taught>100:
        overtime_rate = int(input("enter overtime rate "))
        overtime_hrs = periods_taught - 100
        overtime_salary = overtime_hrs*overtime_rate
        gross_salary = 100*rate_per_period + overtime_salary
    else:
        gross_salary = periods_taught*rate_per_period
    print("Teacher:",name)
    print("Periods:",periods_taught)
    print("Gross salary:",gross_salary)
teacher_salary()