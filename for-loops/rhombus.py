for r in range(1,6):
    for s in range(1,6-r):  # four spaces printed first
        print(" ",end="")
    for c in range(1,6):    # five * printed
        print("*",end="")
    print()