from typing import List
# Pick starting point in outer loop 
# and lengths of different strings for 
# a given starting point 
def all_substrings(word: str) -> List[str]:
    l, res = len(word), []
    # The outer loop controls the length of the substring. 
    for start in range(l+1):
        # This is the end of the substring.
        for end in range(start+1, l+1):
            # End index
            res.append(word[start:end])
    return res

print(all_substrings('abcd'))


