list=["10","20","hello","100","hai","4 00"]
new_list=[]
for d in list:
    try:
        int(d)
        new_list.append(int(d))
    except Exception as e:
        print(e)
print(new_list)
print(sum(new_list))
print(min(new_list))
print(max(new_list))
print(sorted(new_list))

