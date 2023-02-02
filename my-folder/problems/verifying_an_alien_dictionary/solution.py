class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mapper={}
        for i,o in enumerate(order):
            mapper[o]=i
        
        for i in range(len(words)-1):

            for j in range(len(words[i])):

                if j >= len(words[i+1]):
                    return False
                
                if words[i][j]!=words[i+1][j]:
                    if mapper[words[i][j]] > mapper[words[i+1][j]]:
                        return False
                    break
        return True