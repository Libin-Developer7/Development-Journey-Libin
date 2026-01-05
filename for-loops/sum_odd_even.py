number = int(input("enter a number "))
sum_even = 0
sum_odd = 0
for i in range(1,number+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(sum_even)
print(sum_odd)