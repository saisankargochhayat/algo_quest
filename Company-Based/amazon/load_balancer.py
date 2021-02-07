def load_balance(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """   
    if len(arr) < 5:
        return False
    p_sum = [arr[0]] # Calc prefix sum
    for i in range(1, len(arr)):
        p_sum.append(p_sum[-1]+arr[i])
    low = 1
    high = len(arr)-1

    while low < high:
        lower = p_sum[low-1] # Sum of part before low
        higher = p_sum[len(arr)-1] - p_sum[high]
        mid = p_sum[high-1] - p_sum[low]
        # print(lower, mid, higher, low, high)
        if lower == mid == higher:
            return True
        elif lower < higher:
            low += 1
        else:
            high -=1 
    return False




print(load_balance([2, 4, 5, 3, 3, 9, 2, 2, 2]))  
print(load_balance([1,1,1,1]))               
