file_path="file-works\\numbers.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    num=int(line[::-1])
    print(num)