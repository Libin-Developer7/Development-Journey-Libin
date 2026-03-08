def sum_list(nested_list):
    list_sum = 0
    for list in nested_list:
        list_sum += sum(list)
    print(list_sum)
sum_list([[2,4,4],[4,2,4]])