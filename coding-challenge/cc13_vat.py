def your_vat():
    while True:
        try:
            price = int(input("enter price of the item "))
            VAT = int(input("enter VAT in percentage "))
            total_price = price + price*(VAT/100)
            return total_price
        except Exception as e:
            print(e)
print("price including VAT",your_vat())
