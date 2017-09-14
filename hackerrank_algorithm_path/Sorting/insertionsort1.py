#https://www.hackerrank.com/challenges/insertionsort1
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,(input().split())))
    toInsert = arr[len(arr)-1]
    for i in range(len(arr),0,-1):
        # print(i)
        if arr[i-2]>toInsert and (i-2)>=0:
            arr[i-1]=arr[i-2]
            print(*arr)
        elif arr[i-2]<=toInsert:
            arr[i-1]=toInsert
            print(*arr)
            break
        else:
            arr[i-1]=toInsert
            print(*arr)
            break
