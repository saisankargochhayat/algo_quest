def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue

def insertion_sort1(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1]=A[i]
            i = i-1
        A[i+1]=key
        print(A)
    return A

def insertion_sort2(A):
    """
    Sort list A into order, in place.

    From Cormen/Leiserson/Rivest/Stein,
    Introduction to Algorithms (second edition), page 17,
    modified to adjust for fact that Python arrays use 
    0-indexing.
    """
    for j in range(len(A)):
        key = A[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
        print(A)
    return A

alist=[54,26,93,17,77,31,44,55,20]
#insertionSort(alist)
#insertion_sort1(alist)
insertion_sort2(alist)
print(alist)
