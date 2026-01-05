fr_path="file-works\\indian-foods-process\\indian_food.csv"
fr=open(fr_path,'r')
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
# all column names
print(reader.fieldnames)
# first five rows
print([foods for foods in data][:5])
# total no. of foods
print(len(data))
# all unique foods
all_foods=set([foods.get("name") for foods in data])
print(all_foods)
# all unique states
all_states=set([foods.get("state") for foods in data])
print(all_states)
# all flavour profiles
all_flavours=set([foods.get("flavor_profile") for foods in data])
print(all_flavours)
# foods with less than 30 min prep time
low_prep_time_foods=[foods.get("name") for foods in data if int(foods.get("prep_time"))<30]
print(low_prep_time_foods)
# foods with milk in ingredients
foods_with_milk=[foods.get("name") for foods in data if "milk" in foods.get("ingredients").casefold()]
print(foods_with_milk)
# vegetarian foods
veg_foods=[foods.get("name") for foods in data if foods.get("diet").casefold()=="vegetarian"]
print(veg_foods)
# non vegetarian foods
non_veg_foods=[foods.get("name") for foods in data if foods.get("diet").casefold()=="non vegetarian"]
print(non_veg_foods)
# all desserts
all_desserts=[foods.get("name") for foods in data if foods.get("course").casefold()=="dessert"]
print(all_desserts)
# all main courses
all_main_courses=[foods.get("name") for foods in data if foods.get("course").casefold()=="main course"]
print(all_main_courses)
# all sweet foods
all_sweet_foods=[foods.get("name") for foods in data if foods.get("flavor_profile").casefold()=="sweet"]
print(all_sweet_foods)
# all spicy foods
all_spicy_foods=[foods.get("name") for foods in data if foods.get("flavor_profile").casefold()=="spicy"]
print(all_spicy_foods)
# foods with greater than 1 hour cook time
long_cooked_foods=[foods.get("name") for foods in data if int(foods.get("cook_time"))>60]
print(long_cooked_foods)
# count based on flavour profile
all_food_flavours=all_spicy_foods=[foods.get("flavor_profile") for foods in data]
all_flavour_count={f:all_food_flavours.count(f) for f in all_food_flavours}
print(all_flavour_count)
# flavour with highest count
highest_count_flavour=[k for k,v in all_flavour_count.items() if v==max(all_flavour_count.values())]
print(highest_count_flavour)
# food count from each state
foods_by_state=[foods.get("state") for foods in data]
state_food_count={s:foods_by_state.count(s) for s in foods_by_state}
print(state_food_count)
# state with highest food count
highest_food_count_state=[k for k,v in state_food_count.items() if v==max(state_food_count.values())]
print(highest_food_count_state)
# sorting by food names
sorted_foods=sorted(data, key=lambda x:x.get("name"))
print(sorted_foods)