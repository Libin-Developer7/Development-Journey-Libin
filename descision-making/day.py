day = int(input("enter a number between 1 and 7 "))
if day in range(1,6):
    print("WEEKDAY")
elif day in range(6,8):
    print("WEEKEND")
else:
    print("INVALID")