#w.a.p to count vowels in a word
"""word=input("enter a word ")
v_count=0
VOWELS="aeiou"  Capitals since vowels is constant
for ch in word.casefold:
    if ch in VOWELS:
        v_count+=1
        print(v_count) """

def vowel_count(word):
    v_count=0
    VOWELS="aeiou"
    for ch in word.casefold():
        if ch in VOWELS:
            v_count+=1
    return v_count
print(vowel_count("hello"))
print(vowel_count("HELLO"))
