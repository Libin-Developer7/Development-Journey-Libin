# PART A
def list_intersection(list1,list2):
   new_list = [num for num in list1 if num in list2]
   return tuple(new_list)
print(list_intersection([20,30,60,65,75,80,85],[42,30,80,65,68,88,95]))

# PART B
a = range(10000000)
x = set(a)
y = list(a)

import time
target = 9999999
start = time.time()
target in x
end = time.time()
print("Set search time:", end - start)

start = time.time()
target in y
end = time.time()
print("List search time:", end - start)