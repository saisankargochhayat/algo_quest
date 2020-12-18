# Flip the question, think divide, and add. 
class Solution(object):
    def brokenCalc(self, X, Y):
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: 
                Y += 1
            else: 
                Y //= 2
        return ans + X-Y



# DFS
class Solution(object):
    def brokenCalc(self, X, Y):
        def dfs(x, y, memo):
            if x >= y:
                return x - y
            if y % 2 == 0:
                res = dfs(x, y//2, memo) + 1
                return res
            else:
                res = dfs(x, (y+1)//2, memo) + 2
                return res
        return dfs(X, Y)
        
        
        
    
# Starting from X to Y
class Solution(object):
    def brokenCalc(self, X, Y):
        multiple = 1
        res = 0
        while X * multiple < Y:
            multiple *= 2
            res += 1
        diff = X * multiple - Y
        while diff:
            res += diff / multiple
            diff -= diff / multiple * multiple
            multiple /= 2
        return res
