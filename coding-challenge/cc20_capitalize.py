def capitalize(string):
    cap_string = ""
    for w in string.split(" "):
        cap_string += w.capitalize() + " "
    return cap_string
print(capitalize("i love learning"))