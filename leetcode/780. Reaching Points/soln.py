# class Solution(object):
#     def reachingPoints(self, sx, sy, tx, ty):
#         while tx > sx and ty > sy:
#             if tx > ty:
#                 tx %= ty
#             else:
#                 ty %= tx
        
#         if sy == ty and sx <= tx and (tx - sx) % sy == 0:
#             return True
        
#         return sx == tx and sy <= ty and (ty - sy) % sx == 0
        

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy



# Naive back-stepping solution, basically we alternate from tx, ty and 
# step back till  sx, sy
# class Solution(object):
#     def reachingPoints(self, sx, sy, tx, ty):
#         while tx >= sx and ty >= sy:
#             if sx == tx and sy == ty: return True
#             if tx > ty:
#                 tx -= ty
#             else:
#                 ty -= tx
#         return False


# Exhaustive recursive solution
# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         ans = False
#         def helper(x, y):
#             nonlocal ans
#             if x == tx and y == ty:
#                 ans = True
#             # We didn't find answer yet
#             if not ans:
#                 if x + y <= ty:
#                     helper(x, x+y)
#                 if x + y <= tx:
#                     helper(x+y, y)
#         helper(sx, sy)
#         return ans
