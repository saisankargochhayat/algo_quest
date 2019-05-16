# https://www.hackerrank.com/challenges/between-two-sets
#!/bin/python3

import sys

# finds gcd between two numbers


def gcd(x, y):
    if(x == 0):
        return y
    return gcd(y % x, x)

# finds lcm of a array of numbers


def lcm(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ((arr[i] * ans)) / (gcd(arr[i], ans))
    return int(ans)

# finds gcd of a array of numbers


def gcd_array(arr):
    result = 0
    for i in range(len(arr)):
        result = gcd(arr[i], result)
    return int(result)


def getTotalX(a, b):
    count = 0
    gcd_of_b = gcd_array(b)
    lcm_of_a = lcm(a)
    lcm_copy = lcm_of_a
    while(lcm_of_a <= gcd_of_b):
        if(gcd_of_b % lcm_of_a == 0):
            count = count + 1
        lcm_of_a = lcm_of_a + lcm_copy
    return count


def main():
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)


main()
