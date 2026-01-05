for r in range(1,4):
    for c in range(1,4):
        print(f"{r}+{c}={r+c}",end=" ")
    print()
for r in range(1,5):
    for c in range(1,5):
        if r==1 or r==4 or c==1 or c==4:
            print("R",end="")
        else:
            print("S",end="")
    print()
for r in range(1,6):
    for c in range(1,6):
        if r==c or abs(r+c)==6 or abs(r-c)==4:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print("====")
for r in range(1,5):
    for c in range(1,r+1):
        print("1", end=" ")
    for z in range(1,5-r):
        print("0",end=" ")
    print()
print("====")
for r in range(1,6):
    for c in range(1,6):
        if r==1 or r==5 or c==1 or c==5:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print("====")
for r in range(1,6):
    for c in range(1,6):
        if r==3 or c==3:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
print("====")
for r in range(1,5):
    for c in range(1,r+1):
        print("1", end=" ")
    for a in range(1,5-r):
        print("A",end=" ")
    print()
print("====")
for r in range(1,5):
    for c in range(1):
        print("A B C D",end=" ")
    print()
print("====")
for r in range(1,5):
    for c in range(1,5):
        if r==1:
            print("A",end=" ")
        elif r==2:
            print("B",end=" ")
        elif r==3:
            print("C",end=" ")
        elif r==4:
            print("D",end=" ")
    print()
print("====")
for r in range(1,5):
    for c in range(1):
        if r==1:
            print("A B C D",end="")
        elif r==2:
            print("B C D A", end="")
        elif r==3:
            print("C D A B", end="")
        elif r==4:
            print("D A B C", end="")
    print()