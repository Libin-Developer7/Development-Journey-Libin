def make_tuples(lst1,lst2):
    new_list = list()
    for i in range(0,len(lst1)):
        new_list.append((lst1[i],lst2[i]))
    return new_list
print(make_tuples([1,2,3,4],[5,6,7,8]))