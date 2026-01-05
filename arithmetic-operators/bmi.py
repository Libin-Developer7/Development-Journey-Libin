weight_in_kg = int(input("enter weight in kg: "))
height_in_cm = int(input("enter height in cm: "))
height_in_m = height_in_cm/100
BMI = weight_in_kg/(height_in_m**2)
print("your BMI is:",BMI)