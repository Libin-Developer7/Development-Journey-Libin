"""
(1,1) (1,2) (1,3) (1,4)
(2,1) (2,2) (2,3) (2,4)
(3,1) (3,2) (3,3) (3,4)

"""
for r in range(1,4):
    for c in range(1,5):
        print(r,c,end=" ")
    print()

"""
1 2 3 4
1 2 3 4
1 2 3 4

"""
for r in range(1,4):
    for c in range(1,5):
        print(c, end=" ")
    print()