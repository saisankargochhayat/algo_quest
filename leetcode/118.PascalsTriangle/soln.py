class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        for i in range(1,numRows):
            newList = [1]
            for j in range(len(result[i-1])-1):
                newList.append(result[i-1][j]+result[i-1][j+1])
            newList.append(1)
            result.append(newList)
        return result
