words="a man a plan a canal panama"
word_count={}
for ch in words:
    if ch not in word_count:
        word_count[ch]=1
    else:
        word_count[ch]+=1
for k,v in word_count.items():
    if v>1 and k.isalpha():
        print(k)
        
"""words=words.split()
print(words)
words="".join(words)
print(words)"""
    
    