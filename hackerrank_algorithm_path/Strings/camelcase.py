#https://www.hackerrank.com/challenges/camelcase
#!/bin/python3

import sys


s = input().strip()
if len(s)>0:
    counter=1
for i in s:
    if i.isupper():
        counter+=1
print(counter)