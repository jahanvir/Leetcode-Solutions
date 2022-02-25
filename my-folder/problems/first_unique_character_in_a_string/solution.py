class Solution(object):
    def firstUniqChar(self, s):
        
        
        dic=collections.defaultdict(int)
        for c in s:
            dic[c]+=1
        for i,c in enumerate(s):
            if dic[c]==1:return i
        return -1
        
        
            
        """
        :type s: strres
        :rtype: int
        """
        