from itertools import product

x,y = map(int,input().split())
digit = int(input())

l = [j for j in range(x, y+1)]

c = 0

for it in product(l,repeat=digit):
    if sum(it) % 2 == 0:
        c = c + 1
print(c%10000009)