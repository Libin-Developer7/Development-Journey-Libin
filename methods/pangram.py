def is_pangram_text(text):
    is_pangram=True
    ALPHABETS="abcdefghijklmnopqrstuvwxyz"
    for al in ALPHABETS:
        if al not in text:
            is_pangram=False
            break
    return is_pangram

print(is_pangram_text("hello there"))
print(is_pangram_text("The quick brown fox jumps over the lazy dog"))