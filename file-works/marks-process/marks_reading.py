fr_path = "file-works\\marks-process\\python_basics_report.csv"
fr = open(fr_path,"r")
import csv
reader = csv.DictReader(fr)
data = [row for row in reader]
for student in data:
    print(student)
print(len(data))
for student in data:
    print(student["NAME"])
print()
for student in data:
    if student["BATCH "]=="Python":
        print(student["NAME"])
print()
for student in data:
    if student["PRESENT_%"]=="100":
        print(student["NAME"])
for student in data:
    if student["PRESENT_%"]=="100":
        print(student["NAME"],student["MCQ1"])
print(data)
print()
overall_marks = [student.get("OVERALL") for student in data]
max_overall = max(overall_marks)
for student in data:
    if student.get("OVERALL")==max_overall:
        print(student.get("NAME"),student.get("OVERALL"))
print()
for student in data:
    if student.get("OVERALL")!='-' and int(float(student.get("OVERALL")))<30:
        print(student.get("NAME"))
print()
for student in data:
    if "-" in student.values():
        print(student.get("NAME"))
python_students = [ student for student in data if student.get("BATCH ")=="Python"]
print("total python students",len(python_students))
DS_students = [ student for student in data if student.get("BATCH ")=="Data Science"]
print("total DS students",len(DS_students))
for student in data:
    if int(float(student.get("ABSENT_%")))>20:
        print(student)
print()
fw_path = "file-works\\marks-process\\sorted_overall.csv"
fw = open(fw_path,"w")
students_with_complete_data = [student for student in data if student.get("OVERALL")!='-']
sorted_list = sorted(students_with_complete_data, key=(lambda students:int(float(students.get("OVERALL")))), reverse=True)
sorted_names = [fw.write(student.get("NAME")+ "\n") for student in sorted_list]
fw_python_path = "file-works\\marks-process\\python_batch.csv"
fw_python = open(fw_python_path,"w")
python_students_csv = [ fw_python.write(student.get("NAME")+"\n") for student in data if student.get("BATCH ")=="Python"]
fw_DS_path = "file-works\\marks-process\\datascience_batch.csv"
fw_ds = open(fw_DS_path,"w")
ds_students_csv = [ fw_ds.write(student.get("NAME")+"\n") for student in data if student.get("BATCH ")=="Data Science"]
fw_ranklist_path="file-works\\marks-process\\rank_list.csv"
fw_ranklist=open(fw_ranklist_path,"w")
for student in sorted_list[0:3]:
    fw_ranklist.write(student.get("NAME")+"\n")

mcq_xobin_py= [student.get("MCQ_XOBIN") for student in sorted_list if student.get("BATCH ")=="Python" ]
sum_py=0
for m in mcq_xobin_py:
    sum_py+=int(float(m))
avg_py=sum_py/len(mcq_xobin_py)
print("average marks of python students",avg_py)
mcq_xobin_ds= [student.get("MCQ_XOBIN") for student in sorted_list if student.get("BATCH ")=="Data Science" ]
sum_ds=0
for m in mcq_xobin_ds:
    sum_ds+=int(float(m))
avg_ds=sum_ds/len(mcq_xobin_ds)
print("average marks of DS students",avg_ds)
overall_marks=[int(float(student.get("OVERALL"))) for student in sorted_list]
overall_avg = sum(overall_marks)/len(overall_marks)
print("overall average",overall_avg)