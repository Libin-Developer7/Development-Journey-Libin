def palindrome_words(words):
    p_words=[]
    for w in words:
        if w==w[::-1]:
            p_words.append(w)
    return p_words
words=["cat","act","madam","malayalam","racecar"]

print(palindrome_words(words))