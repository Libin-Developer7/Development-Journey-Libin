file_path="file-works\\words.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    line=line.replace(" ","")
    print(line)