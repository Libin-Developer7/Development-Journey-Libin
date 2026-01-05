fr_path="file-works\\titanic-process\\titanic_dataset.csv"
fr=open(fr_path,"r")
import csv
reader = csv.DictReader(fr)
data = [row for row in reader]
print(data)
names=[dic.get("Name") for dic in data]
print(names)
male_count= [ dic.get("Name") for dic in data if dic["Sex"]=="male"]
print(male_count)
genders=[ p.get("Sex") for p in data]
male_count=genders.count("male")
female_count=genders.count("female")
print("male count ",male_count)
print("female count ",female_count)
"""survived= [ p.get("Name") for p in data if p.get("Survived")=="1"]
print("survived ",len(survived))
print(len(names))"""
survived_and_unsurvived=[p.get("Survived") for p in data]
survived_count=survived_and_unsurvived.count("1")
print(survived_count)
usurvived_count=survived_and_unsurvived.count("0")
print(usurvived_count)
total_passengers=len(data)
print(total_passengers)
genders=[p.get("Sex") for p in data]
print("male count",genders.count("male"))
print("female count",genders.count("female"))

all_classes=[p.get("Pclass") for p in data]
class_count={ c:all_classes.count(c) for c in all_classes}
print(class_count)

ages=[int(p.get("Age")) for p in data if p.get("Age").isdigit()]
oldest_age =max(ages)
youngest_age =min(ages)
y_passenger=[ p.get("Name") for p in data if p.get("Age").isdigit() and int(p.get("Age"))==youngest_age]
print(y_passenger)

first_ten = data[:11]
first_ten_names = [p.get("Name") for p in first_ten]
print(first_ten_names)

boarding_stations = [p.get("Embarked") for p in data if len(p.get("Embarked"))>0]
bc = {s:boarding_stations.count(s) for s in boarding_stations}
print(bc)

childrens = [p for p in data if p.get("Age").isdigit() and int(p.get("Age"))<10]
print(len(childrens))
survived_children = [p for p in childrens if p.get("Survived")=='1']
print(len(survived_children))

survived_passengers = [p for p in data if p.get("Survived")=='1']
total_passengers = len(data)
survival_percentage = (len(survived_passengers)/len(data)) * 100
print("survival percentage",round(survival_percentage,2))

total_males = [p for p in data if p.get("Sex")=="male"]
survived_males = [p for p in data if p.get("Survived")=="1" and p.get("Sex")=="male"]
male_survival_rate = (len(survived_males)/len(total_males))*100
print("male survival rate",round(male_survival_rate,2))
total_females = [p for p in data if p.get("Sex")=="female"]
survived_females = [p for p in data if p.get("Survived")=="1" and p.get("Sex")=="female"]
female_survival_rate = (len(survived_females)/len(total_females))*100
print("female survival rate",round(female_survival_rate,2))

classes = [ p.get("Pclass") for p in data ]
class_count = {c:classes.count(c) for c in classes}
print(class_count)
all_survived_class=[p.get("Pclass") for p in data if p.get("Survived")=="1"]
class_survived_count = {c:all_survived_class.count(c) for c in all_survived_class}
print(class_survived_count)
for k,v in class_count.items():
    s_p = class_survived_count.get(k)
    survival_percent = (s_p/v)*100
    print(k,survival_percent)
