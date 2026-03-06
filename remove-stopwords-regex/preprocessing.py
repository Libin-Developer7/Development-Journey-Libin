import re
sentence = "Machine% learning# is a Subset@ of AI"
stopwords_read = open("C:\\Users\\libin_urv2w13\\Desktop\\Development-Journey-Libin\\python-works\\remove-stopwords-regex\\stopwords.txt","r")
stopwords = [w.rstrip("\n") for w in stopwords_read]
sentence = sentence.lower()
sentence = re.sub("[^a-z0-9 ]","",sentence)
print(sentence)
filter_sentence = [w for w in sentence.split(" ") if w not in stopwords]
print(filter_sentence)
refined_word = " ".join(filter_sentence)
print(refined_word)