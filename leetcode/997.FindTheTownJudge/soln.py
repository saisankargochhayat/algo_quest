class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        town = {}
        for i in range(1,N+1):
            town[i] = 0
        for edge in trust:
            x, y = edge
            if town[y] != -1:
                town[y] += 1
            town[x] = -1
        res = []
        for i in town.keys():
            if town[i] == N-1:
                res.append(i)
        return res.pop() if len(res) == 1 else -1

