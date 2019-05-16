# https://www.hackerearth.com/challenge/competitive/february-clash-17/algorithm/sonya-and-sticks/
n = int(input())
indexes = []
heights = []
for i in range(n) :
    a,b = input().split(' ')
    a = int(a)
    b = int(b)
    indexes.append(a)
    heights.append(b)
left = [0]
right = [0]
for i in range(n-1):
    if indexes[i]+heights[i] >= indexes[i+1]:
        left.append(1)
    else:
        left.append(0)pm
    if indexes[i+1] - heights[i+1] <= indexes[i]:
        right.append(1)
    else:
        right.append(0)
left.append(0)
right.append(0)
print(left)
print(right)
