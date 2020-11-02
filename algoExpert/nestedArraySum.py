def nested(arr: list, level: int = 1):
    res = 0
    for ele in arr:
        if type(ele) == int:
            res += ele
        else:
            res += nested(ele, level=level+1)    
    return res*level



print(nested([5,2,[7,-1],3,[6, [-13, 8], 4]]))
print(nested([1,2,3,4,[5]]))