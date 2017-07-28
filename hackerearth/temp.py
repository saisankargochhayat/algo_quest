import math
class segment_tree():
    def __init__(self,mini,maxi):
        self.root = self.build(mini,maxi)
    def build(self,left,right):
        if left == right:
            node = {}
            node['left'] = None
            node['right'] = None
            node['decrements'] = 0
            return node
        else:
            node = {}
            mid = int((left+right)/2)
            node['left'] = self.build(left,mid)
            node['right'] = self.build(mid+1,right)
            node['decrements'] = 0
            return node
    def query(self,node,index,left,right,dec):
        # print("Querying "+str(left)+" "+str(right)+" with dec "+str(dec)+" str index is "+str(index))
        if left==right:
            return node['decrements'] + dec
        else:
            i = index-node['decrements']
            mid = int((left+right)/2)
            if left<=index and index<=mid:
                return self.query(node['left'],index,left,mid,dec+node['decrements'])
            else:
                return self.query(node['right'],index,mid+1,right,dec+node['decrements'])
    def update(self,node,start,end,left,right,dec):
        print("Updating "+str(left)+" "+str(right)+" with start and end "+str(start)+" "+str(end))
        if start>right or end<left:
            return
        if start<=left and right<=end:
            node['decrements'] = node['decrements'] + 1
            return
        dec = dec+node['decrements']
        left = left-dec
        mid = int((left+right)/2)
        self.update(node['left'],start,end,left,mid,dec)
        self.update(node['right'],start,end,mid+1,right,dec)
n = int(input())
l = list(map(int,input().split(' ')))
mini = min(l)
maxi = max(l)
s = segment_tree(mini,maxi)
m = int(input())
for i in range(m):
    k = int(input())
    s.update(s.root,k,n,mini,maxi,0)
ans = []
for i in range(len(l)):
    ans.append(l[i] - s.query(s.root,l[i],mini,maxi,0))
print(*ans)
