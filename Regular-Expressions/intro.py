import re
text = "it is raining in spain"
print(len(re.findall("in",text)))
text = "i have 5 apple i love eating apple"
print(len(re.findall("apple",text)))
print(re.sub("apple","orange",text))
text = "ml$ is$ a$ subset$ of AI"
pattern = "[^a-zA-Z]"
print(re.sub(pattern,"",text))