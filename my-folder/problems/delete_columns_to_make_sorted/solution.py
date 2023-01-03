class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        if not strs or not strs[0]:
            return 0
        
        cols,rows=len(strs[0]),len(strs)
        remove=0
        for i in range(cols):
            for j in range(1,rows):
                if strs[j][i] < strs[j-1][i]:
                    remove += 1
                    break
        return remove

                    
