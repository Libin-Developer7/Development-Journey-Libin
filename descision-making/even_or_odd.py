number = int(input("enter a number "))
if number>0:
    pos_number = number
    if pos_number%2 == 0:
        print("positive even number")
    else:
        print("positive odd number")
else:
    print("not a positive number")

