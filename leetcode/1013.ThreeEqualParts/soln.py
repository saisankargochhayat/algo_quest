class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        totalSum = sum(A)
        if totalSum % 3 != 0:
            return False
        eachPartSum = totalSum//3
        counter = 0
        localSum = 0
        l = len(A)
        for i in range(l):
            if localSum == eachPartSum:
                localSum = 0
                counter += 1
            localSum += A[i]
        if localSum == eachPartSum:
            counter += 1
        return True if counter == 3 else False
