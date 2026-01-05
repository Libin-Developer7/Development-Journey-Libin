file_path="C:\\Users\\libin_urv2w13\\Desktop\\Development-Journey-Libin\\python-works\\file-works\\years.txt"
fw=open(file_path,"w")
for year in range(1800,2026):
    fw.write(str(year)+"\n")