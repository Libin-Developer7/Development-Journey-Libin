# w.a.p to display numbers from 1 to 50, skipping numbers divisible by 4

for i in range(1,51):
    if i%4 == 0:
        continue
    print(i)