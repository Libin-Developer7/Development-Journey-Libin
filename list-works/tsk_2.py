numbers = [10, 20, 30, 40, 50]
sum=0
for num in numbers:
    sum+=num
print(sum)
largest_num=max(numbers)
smallest_num=min(numbers)
print(largest_num)
print(smallest_num)

fruits = ["apple", "banana", "cherry", "apple"]
for f in fruits:
    if fruits.count(f)>1:
        fruits.remove(f)
print(fruits)
reversed_list=numbers[::-1]
print(reversed_list)

marks = [45, 67, 89, 34, 22, 90]
for m in marks:
    if m>50:
        print(m)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))
print(A.intersection(B))
if 2 in A:
    print("2 exists in set A")
else:
    print("2 does not exist in set A")
A.add(7)
A.remove(5)
print(A)
print(A.difference(B))

numbers_1 = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers_1))