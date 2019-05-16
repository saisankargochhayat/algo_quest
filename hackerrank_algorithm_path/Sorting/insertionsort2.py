#https://www.hackerrank.com/challenges/insertionsort2
def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
        print(*alist)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,(input().split())))
    insertionSort(arr)
# print(alist)