story_path="file-works\\word-count\\story.txt"
fr=open(story_path,"r")
word_count={}
for line in fr:
    words=line.split()
    for wrd in words:
        wrd=wrd.rstrip(",")
        wrd=wrd.rstrip(".")
        if wrd in word_count:
            word_count[wrd]+=1
        else:
            word_count[wrd]=1
print(word_count)
max_count=max(word_count.values())
for k,v in word_count.items():
    if v==max_count:
        print(k,v)

