def all_the_same(words):
    if type(words) == str:
        words = words.split(",")
    i=0
    while(i<len(words)-1):
        if words[i] == words[i+1]:
            i+=1
        else:
            return False
    return True

print(all_the_same(["Mary","Mary","Mary"]))