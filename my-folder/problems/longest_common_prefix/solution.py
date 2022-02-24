class Solution(object):
    def longestCommonPrefix(self, strs):
        
        n=len(strs)
        lcp=""
        if n==0 or strs is None:return lcp
        
        minimum=len(strs[0])
        for i in range(1,len(strs)):
            minimum=min(minimum,len(strs[i]))
        for i in range(minimum):
            current=strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i]!=current:
                    return lcp
            lcp+=current
        return lcp
            

        """
        :type strs: List[str]
        :rtype: str
        """
        