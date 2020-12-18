# O(N LogN)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hp = []
        rowLen = len(mat[0])
        for i, row in enumerate(mat):
            hp.append((self.binSearch(row), i))
        return [i for _, i in sorted(hp)][:k]
            
    def binSearch(self, row):
        l, h = 0, len(row)
        
        while l < h:
            mid = l + (h-l)//2
            if row[mid] == 1:
                l = mid+1
            else:
                h = mid
        return l if l <= len(row) else 0
