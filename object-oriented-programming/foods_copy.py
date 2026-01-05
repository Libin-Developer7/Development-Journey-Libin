from copy import copy           # copy/shallowcopy takes copy of only outer objects
from copy import deepcopy       # deepcopy takes copy of outer and inner objects(used for nested collections)
                                
john_fvt_foods=[
    ["dosa","tea"],
    ["meals","lime"],
    ["chapathy","lime"]
]
jacob_fvt_foods=deepcopy(john_fvt_foods) 
jacob_fvt_foods[0][0]="idly"
print(jacob_fvt_foods)
print(john_fvt_foods)

vrinda_fvt_colors=["black","blue","red"] # making copy using "=" results in both var pointing to same object
shiva_fvt_colors=copy(vrinda_fvt_colors)
shiva_fvt_colors.append("purple")
print(vrinda_fvt_colors)
print(shiva_fvt_colors)

