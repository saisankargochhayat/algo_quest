# https://aonecode.com/amazon-online-assessment-oa2-optimize-memory-usage
def binSearch(arr, n):
    pass

def optimizeMemoryUsage(foregroundTasks, backgroundTasks, K):
    """
    :type foregroundTasks: List[int]
    :type backgroundTasks: List[int]
    :type K: int
    :rtype: List[List[int]]
    """                    
    res = set()
    fTask, bTask = list(enumerate(foregroundTasks)), list(enumerate(backgroundTasks))
    fTask.sort(key=lambda x: x[1], reverse=True)
    bTask.sort(key=lambda x: x[1], reverse=True)
    # Lets attempt to pick one task that fit memory
    for index, num in fTask:
        if num <= K:
            target = K-1

            

        

    print(fTask, bTask)

print(optimizeMemoryUsage([1, 7, 2, 4, 5, 6], [1, 1, 2], 10))