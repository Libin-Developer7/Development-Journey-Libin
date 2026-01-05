"""word = input("enter a word ")
VOWELS="aeiou"
cons_count=0
for ch in word.casefold():
    if ch not in VOWELS and ch.isalpha():
        cons_count+=1
print(cons_count)"""

def cons_count(word):
    con_count =0
    VOWELS="aeiou"
    for ch in word.casefold():
        if ch not in VOWELS and ch.isalpha():
            con_count+=1
    return con_count
print(cons_count("powerful"))


        