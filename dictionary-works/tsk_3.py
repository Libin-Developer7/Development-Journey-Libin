sqr_list=[]
for num in range(1,11):
    squares=num**2
    sqr_list.append(squares)
print(sqr_list)

evn_list=[]
for num in range(1,21):
    if num%2==0:
        evn_list.append(num)
print(evn_list)

letter_list=[]
wrd_list=["apple", "banana", "cherry"]
for wrd in wrd_list:
    letter_list.append(wrd[0])
print(letter_list)
caps_list=[]
wrd_list=["apple", "banana", "cherry"]
for wrd in wrd_list:
    caps_list.append(wrd.upper())
print(caps_list)

div_by_3=[]
for num in range(1,31):
    if num%3==0:
        div_by_3.append(num)
print(div_by_3)
len_words=[]
words= ["hi", "hello"]
for wrd in words:
    len_words.append(len(wrd))
print(len_words)

sqr_odds=[]
for num in range(1,16):
    if num%2!=0:
        sqr_odds.append(num**2)
print(sqr_odds)
string="programming"
VOWELS="aeiou"
vwl_list=[]
for ch in string:
    if ch in VOWELS:
        vwl_list.append(ch)
print(vwl_list)
neg_list=[]
for num in range(1,11):
    neg_list.append(-num)
print(neg_list)

mult_five=[]
for num in range(1,51):
    if num%5==0:
        mult_five.append(num)
print(mult_five)

import math
sqrt_num=[]
for num in range(1,11):
    sqr_root=math.sqrt(num)
    sqr_root=f"{sqr_root:.2f}"
    sqrt_num.append(sqr_root)
print(sqrt_num)
words = ["apple", "dog", "cat", "pen"]
a_words=[] 
for wrd in words:
    if "a" in wrd:
        a_words.append(wrd)
print(a_words)
nums = [2, 5, 7]
double_num=[]
for num in nums:
    double_num.append(num*2)
print(double_num)
ends_with_5=[]
for num in range(1,101):
    if num%5==0 and num%10!=0:
        ends_with_5.append(num)
print(ends_with_5)
string="I love python"
wthwt_spc_string=string.replace(" ","")
char_list=[]
for ch in wthwt_spc_string:
    char_list.append(ch)
print(char_list)

fruits= {"apple", "banana", "orange"}
print(fruits)
fruits.add("apple")
print(fruits)
colours= {"red", "green"}
colours.add("blue")
colours.remove("green")
print(colours)
colours.discard("yellow")
languages={"java", "c++", "python", "ruby"}
print("python" in languages)
friend1 = {"cricket", "football", "hockey"}
friend2 = {"tennis", "football", "cricket"}
unq_sport_frnd1=friend1.difference(friend2)
unq_sport_frnd2=friend2.difference(friend1)
print(unq_sport_frnd1)
print(unq_sport_frnd2)
sports_both_like=friend1.intersection(friend2)
print(sports_both_like)
mobile_brands = {"Samsung", "Apple", "OnePlus", "Vivo"}
budget_brands = {"Vivo", "Realme", "OnePlus"}
budget_unfriendly=mobile_brands.difference(budget_brands)
print(budget_unfriendly)
a = {"car", "bike", "bus"}
b = {"bike", "train", "flight"}
print(a.symmetric_difference(b))

text = "Python is easy and Python is powerful"
txt_list= text.split()
txt_set=set(txt_list)
for wrd in txt_set:
    print(wrd)
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
seen= set()
duplicates=set()
for num in numbers:
    if num not in seen:
        seen.add(num)
    else:
        duplicates.add(num)
print(duplicates)

python_students = {"Alice", "Bob", "Charlie"}
ml_students = {"Bob", "David", "Eve"}
both=python_students.intersection(ml_students)
only_python=python_students.difference(ml_students)
all_students=python_students.union(ml_students)
print(both, only_python, all_students)

set_sqr_even=set()
for num in range(1,11):
    if num%2==0:
        squares=num**2
        set_sqr_even.add(squares)
print(sorted(set_sqr_even))

emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com", "d@outlook.com", "b@yahoo.com"]
unique_ids=set(emails)
print(unique_ids)
duplicate_ids=[]
for mail in emails:
    if emails.count(mail)>1 and mail not in duplicate_ids:
        duplicate_ids.append(mail)
print(duplicate_ids)
cart1 = {"Milk", "Bread", "Eggs", "Butter"}
cart2 = {"Bread", "Juice", "Eggs", "Cheese"}
both=cart1.intersection(cart2)
only_one=cart1.symmetric_difference(cart2)
print(both)
print(only_one)
student={}
student["name"]="Rahul"
student["age"]="14"
student["grade"]="B"
print(student)
