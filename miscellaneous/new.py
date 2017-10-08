def binary(a,l,r,x):
	if r>=l:
		mid=int(l+(r-l)/2)
		if a[mid]==x:
			return mid
		elif a[mid]>x:
			return binary(a,l,mid-1,x)
		else:
			return binary(a,mid+1,r,x)

	else:
		return -1



a= []
q=int(input('Enter the number of elements: '))
for x in range(q):
	w=int(input())
	a.append(w)
print(a)
x=int(input('enter element to be found :'))

sorted(a)
index=binary(a,0,q-1,x)
print(index)
# your code goes here
