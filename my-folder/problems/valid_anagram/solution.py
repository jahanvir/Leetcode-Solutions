class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        