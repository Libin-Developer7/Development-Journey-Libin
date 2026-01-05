#1,2,3,4.....20
i=1
while(i<=20):
    if i%3 ==0:
        print("fizz")
    elif i%5 ==0:
        print("buzz")
    elif i%3 ==0 and i%5 ==0:
        print("fizzbuzz")
    i+=1