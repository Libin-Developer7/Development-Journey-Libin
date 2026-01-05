fr_path="error-handling\\numbers.txt"
try:
    fr=open(fr_path,"r")
    data = [line.rstrip("\n")for line in fr]
    new_data=[]
    for d in data:
        try:
            int(d)
            new_data.append(int(d))
        except Exception as e:
             print(e)
        finally:
             fr.close()
    print(max(new_data))
    print(min(new_data))
    print(sum(new_data))
    count={num:new_data.count(num) for num in new_data}
    for k,v in count.items():
        if v==max(count.values()):
            print("most frequent",k,v)
except Exception as e:
            print(e)