"""
:type people: List[List[int]]
:rtype: List[List[int]]

[ ] [ ] [ ] [ ] [4] [ ]    #  [4, 4]: 6 slots, insert 4 with 4 empty space before it
[5] [ ] [ ] [ ]     [ ]    #  [5, 0]: 5 slots, insert 5 with 0 empty space before it
    [ ] [5] [ ]     [ ]    #  [5, 2 - 1]: 4 slots, insert 5 with 1 empty space before it
    [ ]     [6]     [ ]    #  [6, 1]: 3 slots, insert 6 with 1 empty space before it
    [7]             [ ]    #  [7, 0]: 2 slots, insert 7 with 0 empty space before it
                    [7]    #  [7, 1 - 1]: 1 slots, insert 7 with 0 empty space before it
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
	
		# Sort by height ascending, counts descending
        people.sort(key=lambda x: (x[0], -x[1]))
		# Initialize the final list with 0
        ans = [0] * len(people)
		
        for height, num in people:
			# zero_count stores the number of 0s (which is the # of greater numbers) when iterating
			# idx means the index in final list 
            zero_count, idx = 0, 0
			# When the # of 0s reachs the required number, then stop the iteration
			# idx would be the final index
            while zero_count <= num:
                if ans[idx] == 0:
                    zero_count += 1
                idx += 1
			
            ans[idx - 1] = [height, num]
        return ans


    
# # Sort descending, insert tallest people first. 
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #hSorted = sorted(people, key=lambda x: (-x[0], x[1]))
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
