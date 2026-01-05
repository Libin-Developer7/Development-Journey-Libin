file_path="file-works\\perf_num.txt"
fw_perf_num=open(file_path,"w")

def is_perfect_number(num):
    sum_of_divisors=0
    for i in range(1,num):
        if num%i==0:
            sum_of_divisors+=i
        else:
            continue
    if sum_of_divisors==num:
        return True
    else:
        return False
for num in range(1,101):
    if is_perfect_number(num) is True:
        fw_perf_num.write(str(num)+"\n")