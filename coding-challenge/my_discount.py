def my_discount():
    price = int(input("enter the price "))
    discount = int(input("enter the discout "))
    discounted_price = price - ((price*discount)/100)
    return discounted_price
print(my_discount())