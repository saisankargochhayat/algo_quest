class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        tLen, nLen = len(typed), len(name)
        i, j = 0, 0
        while i < nLen and j < tLen:
            if name[i] == typed[j]:
                while j < tLen and (name[i] == typed[j]):
                    if name[i] == typed[j] and (i < nLen - 1):
                        if name[i+1] == typed[j]:
                            j += 1
                            break
                    if name[i] == typed[j]:
                        j += 1
            else:
                return False
            i += 1
        if i < nLen or j < tLen:
            return False
        return True 
