# Largest lexicographical string with at most K consecutive elements
# Given a string S, the task is to find the largest lexicographical string with no more than K consecutive occurrence of an element by either re-arranging or deleting the elements.

# Examples: 

# Input: S = “baccc” 
# K = 2 
# Output: Result = “ccbca” 
# Explanation: Since K=2, a maximum of 2 same characters can be placed consecutively. 
# No. of ‘c’ = 3. 
# No. of ‘b’ = 1. 
# No. of ‘a’ = 1. 
# Since the largest lexicographical string has to be printed, therefore, the answer is “ccbca”.

# Input: S = “xxxxzaz” 
# K = 3 
# Output: result = “zzxxxax” 

def constuctString(word: str, k: int) -> str:
    countArr = [0]*26
    a, ans = ord('a'), []
    for c in word:
        countArr[ord(c)-a] += 1
    i = 25 # start at z
    # Now we have count of all chars we start from z to a.
    while i >= 0:
        # More chars than the window permits
        if countArr[i] > k:
            # Lets append k letters if they exist.
            letter = chr(i+a)
            ans.append(letter*k)
            countArr[i] -= k
            # look for the next element
            j = i-1
            while(countArr[j] <= 0 and j>0):
                j -= 1
            # add one of the next element
            if countArr[j] > 0 and j >= 0:
                letter = chr(j+a)
                ans.append(letter)
                countArr[j] -= 1
            else:
                break # we cant build string more. 
        elif countArr[i] > 0:
            letter = chr(i+a)
            ans.append(letter*countArr[i])
            countArr[i] = 0 
        else:  # this letter we can't do anything, lets skip
            i -= 1
        # print(''.join(ans))

    return ''.join(ans)

res = constuctString("zzzzzzxxxzzaabbazza", 3)
print(res)
print(res == "zzzxzzzxzzzxzbbaaa")