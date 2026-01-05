lst=[1,3,7,8,5]   # map used to apply funcationality to every object in a sequence. map(func, iterable)
squares=list(map(lambda n:n**2,lst))
print(squares)
cubes=list(map(lambda n:n**3,lst))
print(cubes)
add_five=list(map(lambda n:n+5,lst))
print(add_five)

lst1=[2,4,7,9,8,5] # filter used to filter out values following a condition. filter(func/cond, iterable)
evens=list(filter(lambda n:n%2==0,lst1))
print(evens)
odds=list(filter(lambda n:n%2!=0,lst1))
print(odds)
get_five=list(filter(lambda n:n==5,lst1))
print(get_five)

from functools import reduce
lst2=[10,20,30,40,50] # reduce extracts one value following a condition. reduce(func, iterable)
max=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst2) # reduce accepts two arguments
print(max)
min=reduce(lambda n1,n2:n1 if n1<n2 else n2, lst2)
print(min)
product=reduce(lambda n1,n2:n1*n2, lst2)
print(product)

lst3=[10,12,16,18,20]
b_list=list(map(lambda n:n%2==0,lst3))
is_all_even=all(b_list)  # all returns True if every val in a bool list is True
print(is_all_even) 

lst4=["housefull","beautiful","peaceful","harmful","thinkful","powerful"]
b_list=list(map(lambda n:n.endswith("ful"),lst4))
is_all_ful=all(b_list)
print(is_all_ful)

lst5=["program","problem","perfect","apple"]
b_list=list(map(lambda n:n.startswith("pro"),lst5))
is_any_pro=any(b_list)
print(is_any_pro)

# prime_number
number=7
print(not any([number%i==0 for i in range(2,number)]))