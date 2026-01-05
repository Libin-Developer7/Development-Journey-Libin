fr_path="error-handling\\cart\\cart_items_100.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
order_summary={}
for o in data:
    title=o.get("title")
    quantity=int(o.get("quantity"))
    if title in order_summary:
        order_summary[title]+=quantity
    else:
        order_summary[title]=quantity
for k,v in order_summary.items():
    if v==max(order_summary.values()):
        print("max order",k,v)
for k,v in order_summary.items():
    if v==min(order_summary.values()):
        print("min order",k,v)
users=[o.get("user")for o in data]
all_orders={user:users.count(user)for user in users}
for k,v in all_orders.items():
    if v==max(all_orders.values()):
        print(k,v)