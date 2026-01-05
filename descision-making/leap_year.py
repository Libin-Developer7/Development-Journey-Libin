year = int(input("enter year "))
if (year%100 == 0 and year%400 == 0) or (year%100!=0 and year%4 == 0):
    print("leap year")
else:
    print("not leap year")
# century years (last two digits zero) should be divible by 400. Non century years divisible by 4