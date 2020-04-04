# One without delete
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0]
        if n%2 == 0:
            res = []
        for i in range(1,(n//2)+1):
            res.append(i)
            res.append(-i)
        return res

# # One with delete.
# class Solution:
#     def sumZero(self, n: int) -> List[int]:
#         res = [i for i in range(-(n//2),(n//2)+1)]
#         if n%2 == 0:
#             pos = n//2
#             del res[pos]
#         return res
