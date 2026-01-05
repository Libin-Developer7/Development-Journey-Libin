
def is_anagram(word1,word2):
    srt_wrd1=sorted(word1)
    srt_wrd2=sorted(word2)
    return srt_wrd1==srt_wrd2
print(is_anagram("cat","act"))

def is_anagram_sol(word1,word2):
    is_anagram_word=True
    if len(word1)!=len(word2):
        return False
    for ch in word1:
        ch_count_in_w1= word1.count(ch)
        ch_count_in_w2= word2.count(ch)
        if ch_count_in_w1!=ch_count_in_w2:
            is_anagram_word=False
            break
    return is_anagram_word

print(is_anagram_sol("pat","tap"))



    