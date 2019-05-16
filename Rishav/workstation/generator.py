import random
n = random.randrange(1,30)
l = random.randrange(1,20)
a = random.randrange(1,100)
b = random.randrange(a+n*l,10000)
print(1)
print(str(n)+" "+str(l)+" "+str(a)+" "+str(b))
snakes = []
for i in range(n):
    snakes.append(random.randrange(1,1000))
print(' '.join(str(x) for x in snakes))
