def average_calories():
    calories = input("enter daily calories(comma seperated), type 'done' when finished ")
    calorie_list = list(map(int, calories.split(",")))
    avg_calories = sum(calorie_list)/len(calorie_list)
    if input() == "done":
        return avg_calories

print(f"average calories: {average_calories()}")
