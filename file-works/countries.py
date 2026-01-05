"""
f=open(file_path,"r","w"or"a") -> read,write or append
"""

file_path= "C:\\Users\\libin_urv2w13\\Desktop\\Development-Journey-Libin\\python-works\\file-works\\countries.txt"
fr=open(file_path,"r")
for line in fr:
    print(line)
