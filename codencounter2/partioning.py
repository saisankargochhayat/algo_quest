n = input()
dc = [0 for i in range (0, 123)]
length = len(n)
previous = 0
current = 0
concurrency = 0
for i in range(0, length):
    current = ord(n[i])
    if current == previous:
        concurrency += 1
    else:
        if dc[current] < concurrency:
            dc[current] = concurrency
        concurrency = 1
    previous = current
print(max(dc))