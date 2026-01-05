for r in range(1,5):
    for c in range(1,5):
        if r==1 or c==1 or r==4 or c==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  