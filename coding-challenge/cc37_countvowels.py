def count_the_vowels(word):
    word = set(word)
    vowels = "aeiou"
    vowel_count = 0
    for ch in word:
        if ch in vowels:
            vowel_count+=1
    print(vowel_count)
count_the_vowels("saas")