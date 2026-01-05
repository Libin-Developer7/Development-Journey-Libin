menu_items={
    "biriyani":200,
    "paratha":20,
    "appam":20,
    "chicken curry":150,
    "beef fry":150
}

for k in menu_items.keys():
    print(k)
for k,v in menu_items.items():
    print(k,v)
# items under 50
for k,v in menu_items.items():
    if v<50:
        print(k)
# fetch item price
print(menu_items.get("biriyani",0))
# check item and update price

for k,v in menu_items.items():
    if "biriyani" in k:
        menu_items["biriyani"]+=15
print(menu_items)

