# Plain old sorting by difference of A and B. 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l = len(costs)
        # Costs sorted by price difference of sending to A vs B. 
        heap = sorted(costs, key=lambda x:x[0] - x[1])
        # First half elements go to A and second half go to B. 
        return sum([heap[i][0] for i in range(0, l//2)]) + sum([heap[j][1] for j in range(l//2, l)])

# Heap    
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        import heapq
        A, B, l, ans = 0, 0, len(costs)/2, 0
        heap = []
        for cost in costs:
            diff = abs(cost[1] - cost[0])
            heappush(heap, (-diff, cost))
        
        while heap and A < l and B < l:
            _, cost = heappop(heap)
            if cost[0] <= cost[1]:
                A += 1
                ans += cost[0]
            else:
                B += 1
                ans += cost[1]
        
        # Remaining elements
        index = 0 if A < B else 1
        ans += sum([ele[1][index] for ele in heap])
        return ans
