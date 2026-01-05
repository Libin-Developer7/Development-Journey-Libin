
def emi(p,r,n):
    result=(p*r*(1+r)**n)/((1+r)**n -1)
    return result
print(round(emi(25000,0.01,12))) # print is used when return is used