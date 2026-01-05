def display_person(**kwargs):
    print(kwargs)

display_person(name="hari",age=25,place="kakkanad")

def operation(*args,**kwargs):
    op=kwargs.get("key")
    if op=="max":
        print(max(args))
    elif op=="min":
        print(min(args))
operation(10,20,30,key="max")
operation(10,20,30,key="min")

class NumberCount:
    def solution(*args,**kwargs):
        val=kwargs.get("value")
        val_lst=[]
        for values in args:
            val_lst.append(values)
        return val_lst.count(val)

num_count=NumberCount()
print(num_count.solution(10,10,10,10,20,30,40,value=10))

