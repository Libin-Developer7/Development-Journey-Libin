db_pin = 1234
db_balance = 50000
pin = int(input("enter atm pin "))
if pin == db_pin:
    amount = int(input("enter withdrawal amount "))
    if amount <= db_balance:
        print("withdrawal successful")
    else:
        print("insufficient balance")
else:
    print("incorrect pin")
