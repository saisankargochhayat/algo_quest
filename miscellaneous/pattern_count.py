#!/bin/python3

import sys
import re
def patternCount(s):
    # Complete this function
    match=re.findall(r'(?=(10+1))',s)
    # print(match)
    return match
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(len(result))