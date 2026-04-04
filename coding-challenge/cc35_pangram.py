import string
def check_pangram(sentence):
    alphabets = string.ascii_lowercase
    sentence = ("").join(sentence.split(" "))
    for c in alphabets:
        if c not in sentence:
            return False
    return True

print(check_pangram("the quick brown fox jumps over a lazy dog"))