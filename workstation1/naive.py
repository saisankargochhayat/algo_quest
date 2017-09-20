def solution(A, B):
    A.sort()
    B.sort()
    for a in A:
        if a in B:
            return a
    return -1
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
print(solution(A,B))
