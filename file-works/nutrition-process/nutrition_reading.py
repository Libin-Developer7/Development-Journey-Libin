fr_path="file-works\\nutrition-process\\Food_Nutrition_Dataset.csv"
fr=open(fr_path,"r")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# first five rows
first_five=[food for food in data][:5]
print(first_five)
# total rows
total_rows=len(data)
print(total_rows)
# all unique categories and food count
all_categories=[food.get("category") for food in data]
count={cat:all_categories.count(cat) for cat in all_categories}
print(count)
# list of all cakes and pies
all_cakes_and_pies=[food.get("food_name") for food in data if food.get("category")=="Cakes and pies"]
print(all_cakes_and_pies)
# highest calorie food
calories=[float(food.get("calories")) for food in data]
max(calories)
max_clorie_food=[food.get("food_name") for food in data if float(food.get("calories"))==max(calories)]
print(max_clorie_food)
# avg calorie of food
avg_cal=sum(calories)/len(data)
print(avg_cal)
# input a category and display all food types
category=input("enter category ")
foods_by_category=[ food.get("food_name") for food in data if food.get("category").casefold()==category.casefold()]
print(foods_by_category)
# highest protein food
all_protein=[float(food.get("protein")) for food in data]
most_protein=[food.get("food_name") for food in data if float(food.get("protein"))==max(all_protein)]
print(most_protein)
# top five high carb foods
all_carbs={food.get("food_name"):float(food.get("carbs")) for food in data}
sorted_by_carbs=sorted(all_carbs,key=all_carbs.get)[:5]
print(sorted_by_carbs)
# average calories of cakes and vegetables
all_cakes_cal=[float(food.get("calories")) for food in data if food.get("category")=="Cakes and pies"]
avg_cakes_cal=sum(all_cakes_cal)/len(all_cakes_cal)
print(avg_cakes_cal)
all_veg_cal=[float(food.get("calories")) for food in data if food.get("category")=="Vegetables and Vegetable Products"]
avg_veg_cal=sum(all_veg_cal)/len(all_veg_cal)
print(avg_veg_cal)
# food category with most number of foods
all_categories=[food.get("category") for food in data]
count={cat:all_categories.count(cat) for cat in all_categories}
for k,v in count.items():
    if v==max(count.values()):
        print(k,v)