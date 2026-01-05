number = int(input("enter a number "))
if number%2 == 0 and number%3 == 0:
    print("number is divisible by both two and three")
elif number%2 == 0 and number%3 != 0:
    print("number is divisible by two only")
elif number%2 != 0 and number%3 == 0:
    print("number is divisible by three only")    
else:
    print("number is not divisible by two or three")