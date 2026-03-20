def count_words(string):
    word_list = string.split(" ")
    return len(word_list)
print(f"word count:{count_words("i love learning")}")

def count_elements(string):
    char_list = "".join(string.split(" "))
    return len(char_list)
print(f"element_count:{count_elements("i love learning")}")