#https://leetcode.com/discuss/interview-question/365452/Goldman-Sachs-or-OA-2020-or-Shares-Purchase
def Solution(word):
    soln_set = []
    # i points to the first char and j to the last char.
    i, lenofWord = 0, len(word)
    count = 0
    for i in range(0, lenofWord-2):
        j = lenofWord
        # This would break once a word in that sequence is found which doesnt have ABC, starting from the end towards allows us to break sooner.
        while j > i:
            if checkABC(word[i:j]):
                count += 1
                j -= 1
            else:
                break

    print(count)

def checkABC(partWord):
    if 'A' in partWord and 'B' in partWord and 'C' in partWord:
        return True
    else:
        return False

test = ["ABC", "ABCCBA", "PQACBA", "ABBCZBAC"]
for i in test:
    Solution(i)
