treasure={
    "box1":"gold",
    "box2":"silver",
    "box3":"diamond",
    "box4":"platinum"

}

print(treasure["box3"])
treasure["box5"]="iron"
print(treasure)

if "box6" not in treasure:
    treasure["box6"]="copper"
print(treasure)

for k in treasure:
    print(k,treasure[k])
for k in treasure:
    print(k)
all_keys=treasure.keys()   # def keys()
print(all_keys)

for k in treasure.keys():
    print(k)

for v in treasure.values():  # def values()
    print(v)

items = treasure.items()    # def items()
print(items)
for i in treasure.items():
    print(i)
box_value2=treasure.get("box2")  # def get(key)
print(box_value2)

print(treasure.get("box10","empty box"))
print(treasure.get("box10"))

treasure.pop("box4")            # def pop(key)
print(treasure)