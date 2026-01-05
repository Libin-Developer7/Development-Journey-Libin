numbers=[1,34,45,43,24,26,27]
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(even_numbers)
print(odd_numbers)
print("=====")
# squares and cubes
arr=[4,2,6,7]
squares=[]
cubes=[]
for num in arr:
    sqr=num**2
    squares.append(sqr)
    cub=num**3
    cubes.append(cub)
print(squares)
print(cubes)
# w.a.p to create a new list that contain recursive numbers
arr=[10,11,12,13,13,13,8,10,9]
new_arr=[]
for num in arr:
    if arr.count(num)>1 and num not in new_arr:
        new_arr.append(num)
print(new_arr)
#non recursive
non_recursive=[]
for num in arr:
    if arr.count(num)==1 and num not in non_recursive:
        non_recursive.append(num)
print(non_recursive)
        

