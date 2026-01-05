# used to store and organize a group of objects
# list,tuple,set,dictionary
"""
Define:[],object_name=list()
"""
calories=[1200,1300,1450,2000,1700,1200,1200]
print(calories[1])
calories[3]=1350
print(calories)
calories[0]=2000
print(calories)

for i in range(0,len(calories)):
    print(calories[i])
print("======")

for c in calories:
    print(c)
print("======")

for c in calories:
    if c>1300:
        print(c)
print("======")

total=0
for c in calories:
    total+=c
print(total)
print("======")

for c in calories:
    avg_calories = total/len(calories)
print(round(avg_calories))

