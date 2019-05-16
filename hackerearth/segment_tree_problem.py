import math
class segment_tree():
    def __init__(self,a):
        self.a = a
        self.root = self.build(0,len(a)-1)
    def build(self,left,right):
        if left == right:
            node = {}
            node['value'] = self.a[left]
            node['left'] = None
            node['right'] = None
            return node
        else:
            node = {}
            mid = int((left+right)/2)
            node['left'] = self.build(left,mid)
            node['right'] = self.build(mid+1,right)
            node['value'] = min(node['left']['value'],node['right']['value'])
            return node
    def update(self,node,index,new_value,left,right):
        if left==right:
            self.a[index] = new_value
            node['value'] = new_value
        else:
            mid = int((left+right)/2)
            if left<=index and index<=mid:
                self.update(node['left'],index,new_value,left,mid)
            else:
                self.update(node['right'],index,new_value,mid+1,right)
            node['value'] = min(node['left']['value'] , node['right']['value'])
    def query(self,root,start,end,left,right):
        if start>right or end<left:
            return float('inf')
        if start<=left and right<=end:
            return root['value']
        mid = int((left+right)/2)
        return min(self.query(root['left'],start,end,left,mid),self.query(root['right'],start,end,mid+1,right))

n,q = input().split(' ')
n,q = int(n),int(q)
a = list(map(int,input().split(' ')))
s = segment_tree(a)

for i in range(q):
    query,left,right = input().split(' ')
    left,right = int(left)-1,int(right)-1
    if query == 'q':
        print(s.query(s.root,left,right,0,n-1))
    else:
        s.update(s.root,left,right+1,0,n-1)
