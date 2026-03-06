def count_dots(str):
    dot_count = 0
    for w in str:
        if w == ".":
            dot_count+=1
    return dot_count
print(count_dots("h.e.l.p."))