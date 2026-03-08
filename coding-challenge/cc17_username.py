import random
def user_name():
    name = input("enter your name ")
    user_name = name[::-1]
    return f"{user_name}{random.randint(0,9)}"
print(user_name())