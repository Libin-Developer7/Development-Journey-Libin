class Fibonaci:
    def series(self,limit):
        p=0
        c=1
        print(p,end=" ")
        print(c,end=" ")
        for n in range(1,limit-1):          # limit-1 since first two numbers is already printed
            n=p+c
            print(n,end=" ")
            p=c
            c=n     
              
fib = Fibonaci()
fib.series(10)
