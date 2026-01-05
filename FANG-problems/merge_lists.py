class MergeLists:
    def solution(self,arr):
        merged=[]
        merged.append(arr[0])
        for lst in arr:
            if merged[-1][1]>=lst[0]:
                merged[-1][1]=lst[1]
            else:
                merged.append(lst)
        return merged
merge_sol=MergeLists()    
print(merge_sol.solution([[1,5],[4,10],[8,15],[16,20]]))
