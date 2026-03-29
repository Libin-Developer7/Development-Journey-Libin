def longest_word(word_list):
    longest_word = word_list[0]
    for w in word_list:
        if len(w)>len(longest_word):
            longest_word = w
    print([len(longest_word),longest_word])
longest_word(['Java','Javascript','Python'])