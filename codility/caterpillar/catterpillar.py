# Each position of the caterpillar will represent a dierent contiguous subsequence in which
# the total of the elements is not greater than s. Let’s initially set the caterpillar on the first
# element. Next we will perform the following steps:
# • if we can, we move the right end (front) forward and increase the size of the caterpillar;
# • otherwise, we move the left end (back) forward and decrease the size of the caterpillar.
# In this way, for every position of the left end we know the longest caterpillar that covers
# elements whose total is not greater than s. If there is a subsequence whose total of elements
# equals s, then there certainly is a moment when the caterpillar covers all its elements.
def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in range(n):
        while (front < n and total + A[front] <= s):
            total += A[front]
            front += 1  
        if total == s:
            return True,back, front
        total -= A[back]
    return False

print(caterpillarMethod([6,2,7,4,1,3,6],12))