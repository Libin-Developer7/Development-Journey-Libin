"""
raise keyword used to show custom error message
"""
age=int(input("enter age "))
if age<18:
    raise Exception("Invalid Age")
else:
    print("eligible for vote")
age1=int(input("enter age "))
if age1<0:
    raise Exception("Invalid Age")
else:
    print("ok")