# find divisors of a number
# 1,2,3,4...number
number = int(input("enter a number "))
i=1
while(i<=number):
    if number%i ==0:
        print(i)
    i+=1

