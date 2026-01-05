num1 = int(input("enter number1 "))
num2 = int(input("enter number2 " ))
operation = input("select operation +,-,* or / ")

match operation:
    case "+":
        print("addition", num1+num2)
    case "-":
        print("subtraction", num1-num2)
    case "*":
        print("multiplication", num1*num2)
    case "/":
        print("division", num1/num2)
    case _:
        print("invalid")