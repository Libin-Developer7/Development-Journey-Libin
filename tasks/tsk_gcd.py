def gcd(num1,num2):
    small_num=0
    result=1
    if num1<num2:
        small_num=num1
    else:
        small_num=num2
        print(small_num)

    for i in range(1,small_num+1):
        if(num1%i==0) and (num2%i==0):
            result=i
    return result

        

print(gcd(18,20))