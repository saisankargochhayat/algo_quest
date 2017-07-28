import math
t = int(input())
for k in range(t):
    n,l,a,b = list(map(int,input().split(' ')))
    snakes = list(map(int,input().split(' ')))
    snakes.sort()
    first = a
    last = b - n*l +1
    def findsum(start,snakes):
        sumd = 0
        if start > last or start < first:
            return float('inf')
        for i in range(len(snakes)):
            snake = snakes[i]
            target = start + (i*(l))
            sumd += abs(target - snake)
        return sumd


    left = first
    right = last
    # current = float('inf')
    # while(left <= right):
    #     # print("left is "+str(left)+ " right is "+str(right))
    #     mid = int((left+right)/2)
    #     current = findsum(mid,snakes)
    #     leftsum = findsum(mid-1,snakes)
    #     rightsum = findsum(mid+1,snakes)
    #     # print("mid sum is "+str(current)+" left is "+str(leftsum) + " right is "+str(rightsum))
    #     if current > rightsum:
    #         left = mid+1
    #     elif current > leftsum:
    #         right = mid-1
    #     else:
    #         break;

    current = float('inf')
    for i in range(first,last):
        x = findsum(i,snakes)
        # print("For " + str(i) + " it is " + str(x))
        if(x < current):
            current = x
        else:
            break
    print(current)

# def findFirst(matrix):
#     for i in range(len(matrix[0])):
#         for j in range(2):
#             if(matrix[i][j] == '#'):
#                 if(j == 0 && matrix[i][1] == '#' && i<len(matrix[0])-1 && matrix[i+1][0] == '#'):
#                     continue
#                 return [i,j]
#     return [-1,-1]
# t = int(input())
# for i in range(t):
#     n = int(input())
#     matrix = [[],[]]
#     matrix[0] = str(input())
#     matrix[1] = str(input())
#     current = findFirst(matrix)
#     if(current[0] == -1):
#         print('no')
#         continue;
