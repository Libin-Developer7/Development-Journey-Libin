fr_path="file-works\\salary-process\\employee_salary_dataset.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# total no. of rows
print(len(data))
# first five rows
print(data[:5])
# total no. of male and female employees
Male_emp=[emp for emp in data if emp.get("Gender")=="Male"]
print(len(Male_emp))
Female_emp=[emp for emp in data if emp.get("Gender")=="Female"]
print(len(Female_emp))
# all unique departments
all_dep=[emp.get("Department") for emp in data]
print(set(all_dep))
# all unique cities
all_cities=[emp.get("City") for emp in data]
print(set(all_cities))
# avg salary for IT department
IT_dep_salary=[int(emp.get("Monthly_Salary")) for emp in data]
IT_avg_salary=sum(IT_dep_salary)/len(IT_dep_salary)
print(IT_avg_salary)
# salaries of employees with Phd education
Phd_emp=[int(emp.get("Monthly_Salary")) for emp in data if emp.get("Education_Level")=="PhD"]
print(Phd_emp)
# city with most employees
city_count={c:all_cities.count(c) for c in all_cities}
highest_emp=[k for k,v in city_count.items() if v==max(city_count.values())]
print(highest_emp)
# all education levels
ed_level=[emp.get("Education_Level") for emp in data]
print(set(ed_level))
# highest salary employee details
salary_srt=sorted(data, key=lambda x:int(x.get("Monthly_Salary")),reverse=True)
print(salary_srt[0])