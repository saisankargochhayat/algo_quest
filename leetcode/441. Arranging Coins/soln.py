# Binary Search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
            print(left, right, k)
        return right

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         # i * (i+1) < 2 * total => conver to (i+1)**2
#         return (int)((2*n+0.25)**0.5 - 0.5)

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         i, total = 0, 0
#         while total <= n:
#             i += 1
#             total = (i * (i+1))/2
#         return i - 1

# naive
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         rows,i = 0, 1
#         nCopy = n
#         while nCopy >= 0:
#             nCopy -= i
#             if nCopy >= 0:
#                 rows += 1
#             i += 1
#         return rows
