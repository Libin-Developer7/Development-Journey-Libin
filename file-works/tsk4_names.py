fr_path="file-works\\names.txt"
fw_path="file-works\\first_last_char.txt"
fr=open(fr_path,"r")
fw=open(fw_path,"w")
for line in fr:
    name=line.rstrip("\n")
    first_char=name[:1]
    last_char=name[-1:]
    fw.write(first_char+" "+last_char+"\n")

