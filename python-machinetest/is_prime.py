# Q1
def is_prime(num):
    is_prime = True
    if num<2:
        is_prime = False
    for i in range(2,num):
        if num%i == 0 or num<2:
            is_prime = False
    return is_prime
print(is_prime(2))
# Q2
def reverse_num(num):
    reverse_num = 0
    while num>0:
        last_digit = num % 10
        reverse_num = (reverse_num*10) + last_digit
        num = num//10
    return reverse_num
print(reverse_num(135))
# Q3
numbers = [10, 45, 2, 89, 34]
largest = max(numbers)

print(f"The largest element is: {largest}")
# Q4
def vowels_and_cons(string):
    vowels = "aeiou"
    string = string.replace(" ","")
    vowel_count = 0
    cons_count = 0
    for ch in string:
        if ch in vowels:
            vowel_count+=1
        else:
            cons_count+=1
    return f"vowel count:{vowel_count}, consonant count:{cons_count}"
print(vowels_and_cons("love "))
