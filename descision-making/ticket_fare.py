age = int(input("enter your age "))
if age in range(0,5):
    print("ticket is free!")
elif age in range(5,19):
    print("ticket fare is 10.RS")
elif age in range(19,61):
    print("ticket fare is 20.RS")