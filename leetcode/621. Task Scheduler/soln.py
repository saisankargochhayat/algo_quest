class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        task_freq = Counter(tasks)
        sorted_tasks = sorted(task_freq.keys(), reverse=True)
        max_freq = task_freq[sorted_tasks[0]]
        idle_time = max(0, (max_freq-1)*n)
        for i in range(1, len(sorted_tasks)):
            if idle_time < 0:
                break
            idle_time -= min(max_freq-1, task_freq[sorted_tasks[i]])
            
        idle_time = max(0, idle_time)
        return len(tasks) + idle_time


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         import heapq
#         from collections import Counter
#         hp, gTimer, res = [], 0, []
#         taskCount = Counter(tasks)
#         for k in taskCount.keys():
#             heapq.heappush(hp, (-taskCount[k], k, 0))
#         stockPile = []
#         minDelay = 0
#         while len(hp) > 0 or len(stockPile) > 0:
#             print(hp, stockPile)
#             if hp:
#                 quantity, taskName, cooldown = heapq.heappop(hp)
#                 if cooldown < gTimer:  # if no cooldown and we find something
#                     res.append(taskName)
#                     if quantity + 1 < 0:
#                         heapq.heappush((quantity+1, taskName, gTimer + n))
#                     gTimer += 1
#                 else:
#                     stockPile.append((quantity, taskName, cooldown)) 
#                     minDelay = min(minDelay, cooldown)
#             elif stockPile: # if hp is empty
#                 diff = minDelay - gTimer
#                 for i in range(diff):
#                     res.append(None)
#                 for a in stockPile:
#                     heapq.heappush(hp, a)
#                 stockPile = []
#                 minDelay = 0
#                 gTimer += diff
#         print(res)