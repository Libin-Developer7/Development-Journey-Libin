numbers=[1,2,3,4,5,6]
num_squares=[ num**2 for num in numbers if num%2==0]
print(num_squares)
text= "Python programming is very interesting"
text=text.split()
five_char=[ wrd for wrd in text if len(wrd)>5]
print(five_char)
marks= {"Aju": 92, "Binu": 76, "Chandru": 64}
grade={}
for k,v in marks.items():
    if v>90:
        grade[k]="A"
    elif v>70 and v<90:
        grade[k]="B"
    else:
        grade[k]="C"
print(grade)    
text="communication"
VOWELS="aeiou"
unq_vowels={ch for ch in text if ch in VOWELS}
print(unq_vowels)
# grade={k:"A" if v>=90 else "B" if v>=70 else "C" for k,v in marks.items()}
# print(grade)
tuple_num=[ (num,num**3) for num in range(1,31) if num%3==0]
print(tuple_num)
text= ['python', 'django', 'react']
text_output=[wrd[::-1] for wrd in text]
print(text_output)
import math
fact_dict={ num:math.factorial(num) for num in range(1,11)}
print(fact_dict)
nest_list= [[1,2], [3,4], [5,6]]
flat_list=[ num for sub in nest_list for num in sub ]
print(flat_list)
Input=[1,2,3,4,5]
square_odd=[str(num**2) for num in Input if num%2!=0]
print(square_odd)
text="banana"
count={ch:text.count(ch) for ch in text}
print(count)