"""
comprehension is used to create a list/tuple/dict/set from a given collection
comprehension=[return iteration condition]
"""
arr=[10,11,12,13,14,15]
add_five=[num+5 for num in arr]
print(add_five)
even_numbers=[num for num in arr if num%2==0]
print(even_numbers)
odd_numbers=[num for num in arr if num%2!=0]
print(odd_numbers)
# dir(str)
#print(endswith in dir(str))