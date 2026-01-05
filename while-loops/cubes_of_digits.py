number = int(input("enter a number "))
sum = 0
while number!=0:
    digit = number%10
    digit_cube = digit**3
    sum = sum + digit_cube
    number = number // 10
print(sum)