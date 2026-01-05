fr_path="error-handling\\nums.txt"
fr=open(fr_path,"r",encoding="utf-8")
num_list=[]
even_list=[]
for line in fr:
    line=line.rstrip("\n")
    try:
        num=int(line)
        num_list.append(num)

    except Exception as e:
        continue
print(num_list)
for num in num_list:
    if num%2==0:
        even_list.append(num)
num_dict={num:num_list.count(num) for num in even_list}
for k,v in num_dict.items():
    if v==max(num_dict.values()):
        print(k,v)

