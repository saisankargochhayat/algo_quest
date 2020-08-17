class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i, curr = 0, 1 
        while candies > 0:
            if candies - curr >= 0:
                res[i] += curr
            else:
                res[i] += candies
            candies -= curr
            i += 1
            curr += 1
            if i == num_people:
                i = i % num_people
        return res
    
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res
    
