def user_name():
   email = input("enter email id ")
   name = email.split("@")[0]
   return name
print("username:",user_name())