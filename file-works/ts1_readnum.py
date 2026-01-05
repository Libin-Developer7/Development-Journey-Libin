file_path="file-works\\ts1_numbers.txt"
fr=open(file_path,"r")
even_list=[]
odd_list=[]
for line in fr:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list)
print(odd_list)