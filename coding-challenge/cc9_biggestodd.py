def biggest_odd(num_string):
    odd_list = list()
    for num in num_string:
        num = int(num)
        if num%2!=0:
            odd_list.append(num)
    return max(odd_list)
print(biggest_odd('23569'))