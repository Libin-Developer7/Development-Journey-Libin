num1 = int(input("enter number1 "))
num2 = int(input("enter number2 "))
small_number = min(num1,num2)
for i in range(1,small_number+1):
    if num1%i == 0 and num2%i == 0:
        print(i)