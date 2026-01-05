# find common divisors of two number
# num1 =12 and num2 = 24
# 1,2,3,4.....12

num1 = 12
num2 = 24
i=1
while(i<=num1):
    if num1%i==0 and num2%i==0:
        print(i)
    i+=1