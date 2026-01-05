def add_num(num1,num2):
    return num1+num2

print(add_num(2,5))

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(4))

def find_max(a,b,c):
    max_num=a
    if b>a and b>c:
        max_num=b
    elif c>a and c>b:
        max_num=c
    return max_num
print(find_max(8,5,10))

def calculate_area(radius):
    return 3.14*radius**2
print(calculate_area(4))

def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=50:
        return "c"
    else:
        return "F"
print(grade(80))

def multiply(a,b):
    return a*b
print(multiply(2,4))

def power(base,exp):
    return base**exp
print(power(2,4))

def reverse_string(string):
    return string[::-1]
print(reverse_string("hello"))

def is_palindrome(word):
    word=word.casefold()
    return word==word[::-1]
print(is_palindrome("Madam"))

def vowel_count(word):
    count=0
    VOWELS="aeiou"
    for ch in word.casefold():
        if ch in VOWELS:
            count+=1
    return count

print(vowel_count("superman"))

