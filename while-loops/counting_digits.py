number = int(input("enter a number ")) #123
count = 0
while number!=0: #123!=0, #12 != 0, #1!=0
    digit = number%10 #3
    count+= 1 #1
    number = number // 10 #12
print(count)


    