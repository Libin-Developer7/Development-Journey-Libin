import re
text = "i@ have 2 bikes and 1 Car#"
# pattern = "[a-z]" matches all lower case alphabets
# pattern = "[A-Z]" matches all uppercase
# pattern = "[a-zA-Z]" all alphabets
# pattern="[0-9]" all digits
# pattern="[a-zA-Z0-9]" Alpha numeric
pattern = "[^a-zA-Z0-9 ]" # [^'string'] -> excluding ^['string']-> starting with
print(re.findall(pattern,text))
print(re.sub(pattern,"",text))