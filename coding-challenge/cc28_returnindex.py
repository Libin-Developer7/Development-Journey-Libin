def index_position(string):
    index_pos = list()
    for ch in string:
        if ch.islower() == True:
            index_pos.append(string.index(ch))
    return index_pos
print(index_position("LovE"))