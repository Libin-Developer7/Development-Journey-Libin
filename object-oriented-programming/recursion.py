# A function that calls itself is called recursion
def hello_world(limit):
    if limit==0:  # base condition
        return    # return exits the function
    print("Hello, World")
    return hello_world(limit-1)
hello_world(3)

def display_numbers(limit):
    if limit==0:
        return 
    print(limit)
    return display_numbers(limit-1)
display_numbers(15)

def sum_of_n(limit):
    if limit==1:
        return 1
    return limit+sum_of_n(limit-1)
print(sum_of_n(5))
"""
5 + sum_of_n(5-1)
4 + sum_of_n(3)
3 + sum_of_n(2)
2+ (sum_of_n(1)=>returns 1)
"""
def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)
print(factorial(6))
"""
factorial(5)=> 5*facorial(4)
factorial(4)=> 4*facorial(3)
factorial(3)=> 3*facorial(2)
factorial(2)=> 2*(facorial(1)=>returns 1)

"""
def digits_sum(num):
    if num==0:
        return 0
    digit=num%10
    return digit + digits_sum(num//10)
print(digits_sum(222))

def digit_product(num):
    if num==0:
        return 1
    digit=num%10
    return digit*digit_product(num//10)
print(digit_product(555))

def reverse_num(num):
    if num==0:
        return ""
    digit=num%10
    return str(digit)+str(reverse_num(num//10))
print(reverse_num(123))

