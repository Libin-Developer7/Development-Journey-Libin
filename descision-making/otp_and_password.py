db_password = "123pw"
db_otp = 1234
password = input("enter password ")
if password == db_password:
    otp = int(input("enter otp "))
    if otp == db_otp:
        print("login successful")
    else:
        print("incorrect otp")
else:
    print("incorrect password")