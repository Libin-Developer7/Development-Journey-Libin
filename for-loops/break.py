# break - used to exit from loop
#continue - skip current iteration and return to loop
for i in range(1,101):
    if i==50:
        break
    print(i)

for i in range(1,51):
    if i==25:
        continue        # skips 25
    print(i)