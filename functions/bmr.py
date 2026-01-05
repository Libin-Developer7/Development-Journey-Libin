def daily_calorie_expenditure(gender,weight,height,age,activity_level=1.2):
    if gender=="male":
        bmr = 10*weight+6.25*height-5*age+5
    else:
        bmr = 10*weight+6.25*height-5*age-161
    return bmr*activity_level          

print(daily_calorie_expenditure("male",80,175,27))

#daily_calorie_consumption(height,weight,age,gender,activity_level,goal,target,duration) (calories required to achieve goal=gain or loss)

def daily_calorie_consumption(height,weight,age,gender,goal,duration,activity_level=1.2):
        if gender=="male":
            bmr = 10*weight+6.25*height-5*age+5
        else:
            bmr = 10*weight+6.25*height-5*age-161
        if goal=="lose":
            daily_calories=(bmr*activity_level)-500
            weight_loss=2*duration
            print("consume",daily_calories,"to achieve weight loss of",weight_loss,"KG in",duration,"months")
        elif goal=="gain":
            daily_calories=(bmr*activity_level)+500
            weight_gain=2*duration
            print("consume",daily_calories,"to achieve weight gain of",weight_gain,"KG in",duration,"months")

daily_calorie_consumption(198,95,25,"male","gain",2)