def count(word):
    ch_count ={ch:word.count(ch) for ch in word}
    return ch_count

print(count("hello"))