words=["radar","mom","mom","dad","level","madam","dam","madam","malayalam","malayalam","madam"]
# display recursive palindromes
"""pali_count={}
for wrd in words:
    if wrd==wrd[::-1] and wrd not in pali_count:
        pali_count[wrd]=1
    elif wrd in pali_count:
        pali_count[wrd]+=1
for k,v in pali_count.items():
    if v>1:
        print(k)"""

wc={}
for w in words:
    if w==w[::-1]:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
for k,v in wc.items():
    if v>1:
        print(k)
