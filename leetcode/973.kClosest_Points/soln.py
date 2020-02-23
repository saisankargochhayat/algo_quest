import heapq

#python maintians a min heap so we want the minimum elements to 
# be in the heap. So we will store the negaince distance in the heap.
# O(N*logK) and space K.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        euclid = lambda p:-(p[0]**2+p[1]**2)
        heap = []
        for point in points:
            heapq.heappush(heap, (euclid(point), point))
            if len(heap)>K:
                heapq.heappop(heap)
        res = [y for x,y in heap]
        return res
    
    # Naive solution
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     euclid = lambda p:p[0]**2+p[1]**2
    #     res = []
    #     for point in points:
    #         res.append((point,euclid(point)))
    #     res = sorted(res, key=lambda tup:tup[1])
    #     output = [res[point][0] for point in range(K)]
    #     return output
