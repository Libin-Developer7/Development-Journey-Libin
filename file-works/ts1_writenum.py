file_path="file-works\\ts1_numbers.txt"
fw=open(file_path,"w")
for num in range(1,51):
    fw.write(str(num)+"\n")