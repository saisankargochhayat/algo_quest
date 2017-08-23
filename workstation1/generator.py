import random
n = random.randrange(1,100000,1)
k = random.randrange(1,1000000,1)
m = random.randrange(1,1000,1)
print(str(n)+" "+str(k)+" "+str(m))
for i in range(k):
    x = random.randrange(1,n,1)
    y = random.randrange(1,n,1)
    print(str(x) + " "+str(y))
print(" ".join([str(random.randrange(1,n,1)) for j in range(m)]))
