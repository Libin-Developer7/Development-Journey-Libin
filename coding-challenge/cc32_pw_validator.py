def password_validator():
    while True:
        password = input("enter your password: ")
        if len(password)<8:
            print("password is too short. Must be greater than 8 characters")
        elif password.isupper():
            print("Password must contain one lowercase character")
        elif password.islower():
            print("Password must contain one uppercase character")
        elif password.isalpha():
            print("Password must contain a number")
        else:
            return f"your password is {password}"
print(password_validator())