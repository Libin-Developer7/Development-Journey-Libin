def just_digits():
    csv = open("coding-challenge\\cc34_python.csv","r")
    for line in csv:
        words = line.split(" ")
    num_list = list()
    for w in words:
        try:
            num_list.append(str(int(w)))
        except:
            continue
    return num_list

print(just_digits())