words=["radar","level","dam","madam","act","cat"]
palindrome=[w for w in words if w==w[::-1]]
print(palindrome)

words_1=["radar","level","dam","madam","act","cat","radar","level","madam","malayalam"]
palindrome_count={wrd:words_1.count(wrd) for wrd in words_1 if wrd==wrd[::-1]}
print(palindrome_count)


