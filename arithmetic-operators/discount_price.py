initial_price = int(input("enter price:"))
discount = float(input("enter discount in percentage:"))
final_price = initial_price - (initial_price*(discount/100))
print(final_price)