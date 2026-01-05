file_path="file-works\\integers.txt"
fr=open(file_path,"r")
num_list=[]
for line in fr:
    line=line.rstrip("\n")
    num=int(line)
    num_list.append(num)
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
for num in num_list:
    if is_prime(num)==True:
        print(num)
