def unique_number(num_list):
    unique_list = list()
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
    sum_diff = sum(num_list)-sum(unique_list)
    if sum_diff%2 == 0:
        return num_list
    else:
        return unique_list

print(unique_number([1,2,4,5,6,7,8,8]))
