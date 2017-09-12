import sys

limit = 1000000007

def towerColoring(n):
    return (3**(3**n))%limit



n = int(input().strip())
result = towerColoring(n)
print(result)
