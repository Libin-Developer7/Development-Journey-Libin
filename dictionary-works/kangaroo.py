

source_word="technician"
target_word="ten"
sp=0  # source word pointer
tp=0
match=0
while sp<len(source_word) and tp<len(target_word):
    if source_word[sp]==target_word[tp]:
        sp+=1
        tp+=1
        match+=1
    else:
        sp+=1
print(match==len(target_word))

