"""file_path="file-works\\greetings.txt"
fr=open(file_path,"r")
for line in set(fr):
    print(line)"""
file_path="file-works\\greetings.txt"
fr=open(file_path,"r")
st=set()
for line in fr:
   line= line.rstrip("\n")
   st.add(line)
print(st)
