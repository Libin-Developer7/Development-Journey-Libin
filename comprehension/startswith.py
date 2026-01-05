words=["program","python","profession","project","prison","performance"]
list=[ w for w in words if w.startswith("pro")]
print(list)
# words ending with on
list_1=[ w for w in words if w.endswith("on")]
print(list_1)
# number squares
arr=[2,3,4,5,6]
dict={num:num**2 for num in arr }
print(dict)
arr=[10,20,11,20,10,10,20,12,13]
num_count={num:arr.count(num) for num in arr}
print(num_count)
text="programming"
char_count={ch:text.count(ch) for ch in text}
print(char_count)
print("count" in dir(dict))
arr=[2,3,4,5]
total=sum(arr)
result=[total-n for n in arr]
print(result)