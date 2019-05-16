def inequal(a):
	s = 0
	for i in range(len(a)):
		for j in range(i+1,len(a)):
			s = s + abs(a[i] - a[j])
	return s

n = int(input())
k = int(input())
chocolates = []
for i in range(n):
	chocolates.append(int(input()))
chocolates = sorted(chocolates)
minDiff = inequal(chocolates[0:k])
for i in range(1,n-k):
	diff = inequal(chocolates[i:i+k])
	# print(diff)
	if diff < minDiff:
		minDiff = diff
print(minDiff)
