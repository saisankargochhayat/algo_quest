import random
n1 = random.randrange(1,100,1)
n2 = random.randrange(1,100,1)
A = []
B = []
for i in range(n1):
    A.append(random.randrange(1,100,1))
for i in range(n2):
    B.append(random.randrange(1,100,1))
print(' '.join(list(map(str,A))))
print(' '.join(list(map(str,B))))
