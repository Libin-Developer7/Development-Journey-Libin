word="ABBAACCA"
recur={}
for ch in word:
    if ch in recur:
        print(ch,"is the first recursive")
        break
    else:
        recur[ch]=1