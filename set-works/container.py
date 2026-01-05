word1="racecar"
word2="cars"
def container(word1,word2):
    flag=True
    for ch in word2:
        if ch not in word1:
            return False
print(container(word1,word2))

st_word1=set(word1)
st_word2=set(word2)
is_container_word=st_word1.issuperset(st_word2)
print(is_container_word)