#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/akash-and-the-assignment-1-12/description/
def main():
    N,Q=map(int, input().split())
    word=input()
    word="0"+word
    #initialize array with zeros
    A = [[0 for x in range(26)] for y in range(50005)]
    #populating array with Frequencies of each letter
    for i in range(1,N+1):
        x=ord(word[i])-ord("a")
        for j in range(26):
            if j==x:
                A[i][j]=A[i-1][j]+1
            else:
                A[i][j]=A[i-1][j]
    #solving queries
    for i in range(Q):
        left,right,k=map(int, input().split())
        #Counting the Kth smallest character
        K=0
        err=True
        for j in range(26):
            K+=A[right][j]-A[left-1][j]
            if K>=k:
                err=False
                break
        ans=chr(ord("a")+j)
        if err:
            print("Out of range")
        else:
            print(ans)


main()
