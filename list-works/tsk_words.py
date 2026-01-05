words = ["hello","hai","hello","is"]
recur_words=[]
for wrd in words:
    if words.count(wrd)>1 and wrd not in recur_words:
        recur_words.append(wrd)
print(recur_words)

non_recur=[]
for wrd in words:
    if words.count(wrd)==1 and wrd not in recur_words:
        non_recur.append(wrd)
print(non_recur)

even_div_three={i for i in range(1,21) if i%2==0 and i%3==0}
print(even_div_three)

numbers= {1,3,5,7,9,11}
numbers.discard(1)
numbers.discard(2)
print(numbers)
numbers.remove(3)
#numbers.remove(4) # 'remove' shows error if number is not in set
print(numbers)

"""A frozenset in Python is just like a set, but it is immutable — 
meaning you cannot change it (no adding or removing elements) after it’s created."""

numbers_frzn = [1, 2, 3, 4, 5]

frozen = frozenset(numbers_frzn)

print(frozen)

frozenset({1, 2, 3, 4, 5})
# try to modify it:

#frozen.add(6)        Try to add an element

# shows AttributeError: 'frozenset' object has no attribute 'add'

s1 = "python"
s2 = "typhon"
is_anagram=True
set_1 = set(s1)
set_2 = set(s2)
set_diff=set_1.difference(set_2)
if len(set_diff)==0 and len(set_1)==len(set_2):
    is_anagram
else:
    is_anagram=False
print(is_anagram)

a = {1, 2}
b = {2, 3}
c = {3, 4}
d = {4, 5}
unq_elements= (a.difference(b)).union(b.difference(c).union(c.difference(d)))

data = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
cmn_1_and_2= data[0].intersection(data[1])
cmn_2_and_3=data[1].intersection(data[2])
cmn_1_and_3 =data[0].intersection(data[2])
cmn_elements= (cmn_1_and_2.intersection(cmn_2_and_3)).intersection(cmn_1_and_3)
print(cmn_elements)