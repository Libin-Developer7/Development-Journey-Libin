def sort_words(string):
    string = string.replace(" ","")
    string = sorted(string)
    str_list = list()
    for ch in string:
        if ch not in str_list:
            str_list.append(ch)
    print(str_list)
    
sort_words("love life")