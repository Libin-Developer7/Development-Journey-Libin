weight_in_kg = int(input("enter weight in kg: "))
height_in_cm = int(input("enter height in cm: "))
height_in_m = height_in_cm/100
bmi = weight_in_kg/(height_in_m**2)
bmi = round(bmi,0)

if bmi in range(0,20):    # Range(start,stop) function returns a sequence of numbers from 'start" to 'stop-1'
    print("UNDERWEIGHT")   
elif bmi in range(20,25):
    print("NORMAL")
elif bmi in range(25,30):
    print("OVERWEIGHT")
else:
    print("OBESE")
