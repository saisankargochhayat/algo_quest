n,k = map(int,input().split())
A=list(map(int,input().split()))
#array to store the count
M=[0]*k
for a in A:
    M[a%k]+=1
count=M[0]*(M[0]-1)//2
for i in range(1,(k+1)//2):
    count+=M[i]*M[k-i]
if(k%2==0):
    count+=M[k//2]*(M[k//2]-1)//2
print(count)

# For any divisor k, you can get k different remainders : 0, 1, 2 .. (k-1). The idea is to count the number of elements with specific remainder.
# Suppose the list is 14 4 7 9 8 3 17 12 and k = 4. Then
# Remainder       Integers        Count
# ---------       ---------       ------
#     0           4, 8, 12        3
#     1           9, 17           2
#     2           14              1
#     3           3, 7            2
# Now, just knowing the count for each value of remainder let's us calculate the required answer. Mathematics behind calculations :
# • Values with remainder 0, can be paired with themselves. That's because even after addition the remainder will remain 0. If there are c such integers, no. of pairs = c*(c-1)/2
# • Values with remainder r can be paired with values with remainder k-r, since, remainder of sum becomes k i.e. 0. In above example, values with remainder 1 and 3 can be paired : (9,3), (9,7), (17,3), (17,7). Total number of pairs = product of counts.
# • Finally, values with remainder exactly k/2, can be paired with themselves (Calculation same as remainder 0 values).
