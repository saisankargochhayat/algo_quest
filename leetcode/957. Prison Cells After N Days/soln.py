# Figuring out the cycle. 
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = dict()
        is_forwarded_flag = False
        while N:
            # We check for repetitions here
            if not is_forwarded_flag:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N 
                    cycle_length = seen[state_key] - N
                    # Fast forwarding done here - 
                    N = N % cycle_length
                    is_forwarded_flag = True
                else:
                    seen[state_key] = N
            
            # Finding the next iteration. 
            if N > 0:
                N -= 1
                next_cells = Solution.nextCell(cells)
                cells = next_cells
        return cells
        
    @staticmethod
    def nextCell(cells) -> List[int]:
        newcell = [0]
        for i in range(1, len(cells)-1):
            newcell.append(int(cells[i-1] == cells[i+1]))
        newcell.append(0)
        return newcell
    
# Bitmap Solution - 
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        # step 1). convert the cells to bitmap
        state_bitmap = 0x0
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        # step 2). run the simulation with hashmap
        while N > 0:
            if not is_fast_forwarded:
                if state_bitmap in seen:
                    # the length of the cycle is seen[state_key] - N 
                    N %= seen[state_bitmap] - N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap] = N
            # if there is still some steps remained,
            #   with or without the fast-forwarding.
            if N > 0:
                N -= 1
                state_bitmap = self.nextDay(state_bitmap)

        # step 3). convert the bitmap back to the state cells
        ret = []
        for i in range(len(cells)):
            ret.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1

        return reversed(ret)


    def nextDay(self, state_bitmap: int):
        state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
        state_bitmap = state_bitmap & 0x7e  # set head and tail to zero
        return state_bitmap
        

from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for i in range(N):
            newCells = [0]*len(cells)
            for j in range(1, len(cells)-1):
                if (cells[j-1] + cells[j+1]) % 2 == 0:
                    newCells[j] = 1
            cells = newCells
                
        return cells

s = Solution()
print(s.prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000))