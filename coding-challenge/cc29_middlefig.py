def middle_figure(a,b):
    a = a.replace(" ","")
    b = b.replace(" ","")
    joined = a + b
    print(joined)
    print(len(joined))
    mid = len(joined) // 2
    print(joined[mid])
middle_figure("make love","not ")
