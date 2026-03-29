def middle_figure(a,b):
    a = a.replace(" ","")
    b = b.replace(" ","")
    joined = a + b
    if len(joined)%2 == 0:
        return "no middle figure"
    else:
        mid = len(joined) // 2
        return joined[mid]

print(middle_figure("make love","not wars"))
