def palindrome(word):
    is_palindrome=True
    word=word.casefold()
    reversed_word=word[::-1]
    if word==reversed_word:
        return is_palindrome
    else:
        is_palindrome=False
        return is_palindrome
    
print(palindrome("Madam"))

def is_palindrome(word):
    word=word.casefold()
    return word==word[::-1]
print(is_palindrome("Madam"))

# string
    # pangram
    # anagram
    # palindrome
    # kangarooword
    # longest sequential palindrome in a given string
    # merge string  wrd1 = ABC wrd2 = PQR mrg=APBQCR