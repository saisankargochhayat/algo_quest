# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    maximum = 0
    S = S.replace('?','.').replace('!','.')
    sentences = S.split('.')
    # print(sentences)
    lengthOfWords = []
    for sent in sentences:
        sent = sent.strip().split()
        lengthOfWords.append(len(sent))
    return max(lengthOfWords)

print solution('Forget  CVs..Save time . x x')