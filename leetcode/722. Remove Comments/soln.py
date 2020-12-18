class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        inBlock, buffer = False, ''
        for line in source:
            p = 0 # line pointer
            while p < len(line):  # We process each line
                curr = line[p]
                # Check for //
                if curr == "/" and p+1 < len(line) and line[p+1] == "/" and not inBlock:
                    p = len(line)
                # check for /*
                elif curr == "/" and p+1 < len(line) and line[p+1] == "*" and not inBlock:
                    inBlock = True
                    p += 1 # as it might end in same line 
                # check for */
                elif curr == "*" and p+1 < len(line) and line[p+1] == "/" and inBlock:
                    inBlock = False
                    p += 1             # we skip * and /         
                elif not inBlock:
                    buffer += curr
                p += 1  # next char

            if buffer and not inBlock:
                res.append(buffer)
                buffer = ''
        return res
                
        
        
        
