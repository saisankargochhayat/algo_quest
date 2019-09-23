class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        bestPos = None
        maxDistance = 0
        counter = 0
        prev = 0
        iEncountered = False
        for i in range(len(seats)):
            if seats[i] == 1:
                if iEncountered:
                    diff = (i - prev)//2
                else: diff = i-prev
                maxDistance = max(diff, maxDistance)
                counter = 0
                prev = i
                iEncountered = True
            else:
                counter += 1
        maxDistance = max(counter, maxDistance)  
        return maxDistance
        
