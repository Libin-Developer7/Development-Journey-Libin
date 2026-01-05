# class ClosestNumberToZero:
#     def solution(self,arr):
#         closest_number=0
#         d={num:abs(num-closest_number) for num in arr}
#         print(d)
#         g=[k for k,v in d.items() if v==min(d.values())]
#         print(max(g))
# closestnumber=ClosestNumberToZero()
# closestnumber.solution([-1,-2,2,1,3,4])
class ClosestNumberToZero:
    def solution(self,arr):
        closest_number=arr[0]
        for num in arr:
            if abs(num)<abs(closest_number): # least number
                closest_number=num # -1
            if closest_number<0 and abs(closest_number) in arr: # returns max value
                return abs(closest_number)
closestnumber=ClosestNumberToZero()
print(closestnumber.solution([-1,-2,2,1,3,4]))


