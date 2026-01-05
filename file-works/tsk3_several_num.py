file_path="file-works\\several_num.txt"
file_path_write="file-works\\last_digit.txt"
fr=open(file_path,"r")
fw=open(file_path_write,"w")
for line in fr:
    num=(line.rstrip("\n"))
    last_digit=num[-1:]
    fw.write(last_digit+"\n")
    
