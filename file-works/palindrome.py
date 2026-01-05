file_path="file-works\\palindrome.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    line=line.replace(" ","")
    if line==line[::-1]:
        print(line)