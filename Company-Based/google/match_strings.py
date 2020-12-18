# Given two strings a, b.

# Check if they are equal, if we can do the following operations.

# swap any even indices of same string. eg swap(a[2], a[4]), swap(b[6], b[0])
# swap odd indices of the same string.
# eg:
# string a: "abad"
# string b: "adab"
# swap(b[1], b[3])

# Answer: true.

# eg: "abcd", "dcba"
# Answer: false.

def checkStr(a, b):
    from collections import defaultdict
    odd = defaultdict(int)
    even = defaultdict(int)
    for i, c in enumerate(a):
        if i % 2 == 0:
            even[c]+=1
        else:
            odd[c]+=1
    for i, c in enumerate(b):
        if i % 2 == 0:
            if even.get(c) != None and even.get(c) > 0:
                even[c] -= 1
            else:
                return False
        else:
            if odd.get(c) != None and odd.get(c) > 0:
                odd[c] -= 1
            else:
                return False
    return True




print(checkStr("abad", "dcba"))
print(checkStr("abad", "abad"))
print(checkStr("aaaa", "aaaa"))