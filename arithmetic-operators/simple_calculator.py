num1= int(input("enter first number:"))
num2= int(input("enter second number:"))
operator = input("select operator: add, subtract, multiply, divide ")
if operator == "add":
    result = print(num1 + num2)
elif operator == "subtract":
    result = print(num1-num2)
elif operator == "multiply":
    result = print(num1*num2)
else:
    result = print(num1/num2)            
