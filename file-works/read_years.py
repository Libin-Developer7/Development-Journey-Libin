file_path="C:\\Users\\libin_urv2w13\\Desktop\\Development-Journey-Libin\\python-works\\file-works\\years.txt"
fr=open(file_path,"r")
year_lst=[]
for line in fr:
    year=int(line.rstrip("\n"))
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        year_lst.append(year)
print(year_lst)

    