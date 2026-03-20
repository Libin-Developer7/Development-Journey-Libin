def simple_calculator():

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation selected.")
            return
        print(f"The result is: {result}")

    except ZeroDivisionError as e:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")
    except NameError as e:
        print("Error: A name error occurred (check if variables are defined).")

simple_calculator()