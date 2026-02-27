def odd_even(num_list):
    odd_list = [num for num in num_list if num%2!=0]
    even_list = [num for num in num_list if num%2==0]
    print(max(even_list) - min(odd_list))
odd_even([1,2,4,6])
