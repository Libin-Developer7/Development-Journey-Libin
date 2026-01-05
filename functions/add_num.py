def add_num(num1,num2):
    result = num1+num2
    print(result)

add_num(10,20)
add_num(130,20)

# odd or even

def chk_number(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    
print(chk_number(7))

# check number is positive or negative

def is_positive(num1):
    if num1>=0:
        return True
    else:
        return False

def is_negative(num2):
    if num2>=0:
        return False
    else:
        return True
    
print(is_positive(10))
print(is_negative(-5))

# funcion max_two-largest number
# function min_two smallest number

def max_two(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
def min_two(num1,num2):
    if num1>num2:
        return num2
    else:
        return num1

print(max_two(1,5))
print(min_two(2,7))

#leap year

def is_leap_year(year):
    if(year%100 == 0 and year%400==0) or (year%100!=0 and year%4==0):
        return True
    else:
        return False
print(is_leap_year(2024))

#bmi

def bmi(weight_in_kg,height_in_cm):
    height_in_m = height_in_cm/100
    result = weight_in_kg/height_in_m**2
    return result

print(round(bmi(80,198)))     