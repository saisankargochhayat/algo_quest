#https://www.interviewbit.com/problems/partitions/
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if(sum(B)%3!=0):
            return 0
        s=sum(B)//3
        pre=[0]*(A)
        suf=[0]*(A)
        for i in range(A):
            pre[i]=pre[i-1]+B[i]
        temp=0
        for i in range(A-1,-1,-1):
            temp+=B[i]
            if(temp==s):
                suf[i]=1
        print(pre, suf)
        ans=0
        for i in range(A):
            if(pre[i]==s):
                for j in range(i+2,A):
                    if(suf[j]==1):
                        ans+=1
        return ans