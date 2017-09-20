def elementToDelete(arr):
    minloss = 100000000000
    elementIndex = 0
    for i in range(len(arr)):
        j=arr[i]
        loss = arr.count(j-1)*j-1 + arr.count(j+1)*j+1
        if (loss < minloss):
            minloss=loss
            elementIndex = i
    return elementIndex


def main():
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    sumOfRamesh=0
    m=0
    arr.sort()
    while(len(arr)):
        m=elementToDelete(arr)
        sumOfRamesh = sumOfRamesh+arr[m]
        y=arr[m]-1
        z=arr[m]+1
        #remove all element before it 
        arr=list(filter(lambda a: a != y, arr))
        #remove all elements after it
        arr=list(filter(lambda a: a != z, arr))
        del(arr[m])
    print(sumOfRamesh)
main()