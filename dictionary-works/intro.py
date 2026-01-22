specs={"laptop":"hp","ram":"16gb","graphics":"radeon","ssd":"500gb","os":"windows"}
print(specs["laptop"])
print(specs["os"])
specs["browser"]="chrome"
print(specs)

product={"code":1100,"title":"shirt","category":"clothes","price":2000,"avl_qty":100}
print(product["title"])
print(product["price"])
product["store"]="kalyan"
print(product)
print("price" in product)
if "category" in product:
    print(product["category"])
else:
    print("not exist")

# add avl_qty as 15 if avl_qty not exist, else update avl_qty as current qty+10
if "avl_qty" in product:
    product["avl_qty"]+=10
else:
    product["avl_qty"]=15
print(product)