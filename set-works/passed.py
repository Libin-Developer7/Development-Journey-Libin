all_students={"hari","ram","rebin","ahan","dibin","deepu"}
passed_students={"hari","ram","dibin"}

failed_students=all_students.difference(passed_students)
print(failed_students)