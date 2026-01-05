age = int(input("enter age "))
if age>=18:
    test = input("is test passed? ")
    if test == 'yes':
        print("liscence approved")
    else:
        print("test not cleared")
else:
    print("not eligible due to age")