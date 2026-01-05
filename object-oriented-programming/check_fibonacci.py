class IsFibonacciNum:
    def solution(self,num):
        p=0
        c=1
        n=p+c
        while(n<num):
            p=c
            c=n
            n=p+c
            if n==num:
                print(True)

fibo=IsFibonacciNum()
fibo.solution(7)
