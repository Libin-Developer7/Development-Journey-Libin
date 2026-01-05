text="this is a python program for word count this program is simple"
split_text=text.split()
word_count={ w:split_text.count(w) for w in split_text}
print(word_count)

def solve(s):
    wrd_lst=s.split()
    capitalized=[]
    print(wrd_lst)
    for wrd in wrd_lst:
         wrd=wrd.capitalize()
         capitalized.append(wrd)
    return(" ".join(capitalized))

txt_list=["hi","hello","heavy","big"]
print(" ".join(txt_list))