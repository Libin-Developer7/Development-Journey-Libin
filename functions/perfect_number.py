def is_perfect_number(number):
    flag = True
    divisor_sum =0
    for i in range(1,number):
        if number%i==0:
            divisor_sum += i
    print(divisor_sum)
    if divisor_sum == number:
        return flag
    else:
        flag = False
        return flag
print(is_perfect_number(4))

