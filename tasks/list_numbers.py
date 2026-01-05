arr = [1, 5, 7, 9, 12, 15, 16, 19, 20]
for num in arr:
    if num%2==0:
        print(num)
print("=====")
for num in arr:
    if num%2!=0:
        print(num)
print("=====")
count_even=0
for num in arr:
    if num%2==0:
        count_even+=1
print(count_even)
print("=====")

count_odd=0
for num in arr:
    if num%2!=0:
        count_odd+=1
print(count_odd)

# task 2
years = [2021, 1999, 1920, 2024, 1852, 1991, 2026, 2000, 2023, 2016, 2009]
for yr in years:
    if(yr%100==0 and yr%400==0) or (yr%100!=0 and yr%4==0):
        print(yr)