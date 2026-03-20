def add_hash(str):
    hash_str = ""
    for ch in str:
        hash_str+= ch+'#'
    hash_str = hash_str.rstrip('#')
    return hash_str

def add_underscore(str):
    underscr_str = str.replace('#','_')
    return underscr_str

def remove_underscore(str):
    remove_underscore = str.replace('_',"")
    return remove_underscore

print(remove_underscore(add_underscore(add_hash("Python"))))