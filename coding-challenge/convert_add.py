def convert_add(str_lst):
    int_lst = list()
    for s in str_lst:
        int_lst.append(int(s))
    return sum(int_lst)
print(convert_add(["1","3","6"]))
