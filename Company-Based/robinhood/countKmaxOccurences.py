def counts(string, word):
    if not string:
        return 0, 0
    count = 0
    idx = 0
    while idx < len(string):
        if len(string[idx:]) < len(word):
            break
        for char_str, char_word in zip(string[idx:], word):
            if char_str != char_word:
                return count, idx
        else:
            count += 1
            idx += len(word)
    return count, idx

def findK(string, word):
    idx = 0 
    max_count = 0
    while idx < len(string):
        if string[idx]==word[0]:
            print(counts(string[idx:], word))
            count, offset = counts(string[idx:], word)
            max_count = max(max_count, count)
            if offset:
                idx += offset
                continue
        idx += 1
    return max_count
    
def maxKOccurrences(sequence, words):
    res = []
    for word in words:
        res.append(findK(sequence, word))
    return res