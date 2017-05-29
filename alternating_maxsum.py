# Alternating Maximum Sum
# Given array consisting of N integers, now your task is to choose some elements ( at least one ) from the array without changing the order of the elements. (Basically, you have to choose any subset of array)

# Such That :

# 1 : The sequence have to be odd-even or even-odd (if first element is even/odd then second have to be odd/even and so on )

# 2 : No two elements in the chosen subset have any common digit.

# You have to output the maximum sum ( sum of all elements present in the chosen subset ) you can obtained by choosing any subset satisfying the above given requirements.

# Input

# The first line contain N ( Size of array )

# The second line consist of N integers

# Output

# Output the maximum sum

# Constraints

# 1 <= N <= 1000

# 1 <= array[i] <= 109

# Sample Input
# 5
# 20 10 6 4 79
# Sample Output
# 99
# Explanation
# Subset : { 20 , 79 } = 20 + 79 = 99
# */
n=int(input())
m=list(map(int, input().split()))