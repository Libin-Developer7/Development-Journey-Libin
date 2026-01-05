start = int(input("enter starting number "))
stop = int(input("enter which number to stop "))

if start<stop:
    for num in range(start,stop+1):
        print(num)
else:
    for num in range(start,stop-1,-1):
        print(num)
