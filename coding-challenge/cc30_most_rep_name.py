# PART A
def repeated_name(name_list):
    name_count = dict()
    for name in name_list:
        if name in name_count:
            name_count[name]+=1
        else:
            name_count[name]=1
    for k,v in name_count.items():
        if v == max(name_count.values()):
            print(k)
repeated_name(["john","peter","john","peter","jones","peter"])

# PART B
def sorted_name(name_list):
    sorted_names = [name.split(" ")[1] + " " + name.split(" ")[0] for name in name_list]
    print(sorted(sorted_names))
sorted_name(['Beyonce Knowles','Alicia Keys','Katie Perry','Chris Brown','Tom Cruise'])

