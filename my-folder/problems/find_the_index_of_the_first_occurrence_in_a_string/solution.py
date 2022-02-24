class Solution(object):
    def strStr(self, haystack, needle):
        #n=len(haystack)
        nl=len(needle)
        if nl==0:return 0
        if haystack==needle:return 0
        for i in range(len(haystack)):
            if haystack[i:i+nl]==needle:return i
        return -1
                
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        