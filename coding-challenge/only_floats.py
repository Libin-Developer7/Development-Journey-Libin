def only_floats(a,b):
    result = 0
    if type(a) == float:
        result += 1
    if type(b) == float:
        result +=1
    return result
print(only_floats(12.1,23))
