number = int(input("enter a number "))
count_odd = 0
count_even = 0
for i in range(1,number+1):
    if i%2!=0:
        count_odd+=1
    else:
        count_even+=1
print("odd count",count_odd)
print("even count",count_even)
