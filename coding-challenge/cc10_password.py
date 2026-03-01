def hide_password():
    password = input("enter your password ")
    for w in password:
       password = password.replace(w,'*')
    return f"{password} your password is {len(password)} characters long"
print(hide_password())