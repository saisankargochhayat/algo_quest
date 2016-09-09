import queue
def main():
    n=int(input())
    q = queue.Queue()
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    #convert list elements to numbers
    list1 = [ int(x) for x in list1 ]
    time=0
    for i in list1:
        q.put(i)
    for x in list2:
        while 1:
            temp=q.get()
            if temp==x:
                time+=1
                break
            else:
                q.put(temp)
                time+=1
    print(time)

main()
