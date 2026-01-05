orders=["tea","coffee","dosa","biriyani"]
orders.append("paratha")  # append(value)->adds to last element
print(orders)
orders.insert(2,"upma") # insert(index,value)
print(orders)
orders.pop(2)          # pop(index) default=-1 popped elemnt is also stored
print(orders)
orders.remove("dosa")  # remove(value)
print(orders)
pos=orders.index("biriyani") # index(value)->returns first index of value
print(pos) 
freq=orders.count("paratha") # count(value)->returns number of occurence of value
print(freq)
orders.reverse()
print(orders)
orders.sort()
print(orders)
fvt_colours=["black","white","red"]
fvt_colours_1=fvt_colours.copy() # new object is created. while in "=" no new object is created
print("favourite",fvt_colours)
print("favourite1",fvt_colours_1)