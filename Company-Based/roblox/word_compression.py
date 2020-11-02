def compressWord(word: str, k: int):
    # Lets define a stack to maintain stream of letters. 
    from collections import deque
    stck = deque([])
    for c in word:
        if stck:
            old_c, val = stck[-1]
            if old_c == c:
                stck.append((c, val+1))
            else:
                stck.append((c, 1))
        else:
            stck.append((c, 1))
        # Now we check if top element has been repeated k times and remove it. 
        old_c, val = stck[-1]
        if val == k:
            # Remove k elements
            for i in range(k):
                stck.pop()
    cArray = [c for c, v in stck]
    return ''.join(cArray)
    


# print(compressWord("abbcccb", 3))
print(compressWord("aba", 2))