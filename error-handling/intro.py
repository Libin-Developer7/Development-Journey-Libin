"""Exception handles only and all runtime errors such as zerodivisionerror, filenotfound, keyerror, valueerror
"""
num1=int(input("enter number1 "))
num2=int(input("enter number2 "))
try:
    result=num1/num2
    print(result)
except Exception as e:
    print(e)
finally:
    print("file operation")
    print("database commit")