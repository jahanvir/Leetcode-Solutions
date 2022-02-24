class Solution(object):
    def reverseString(self, s):
        n=len(s)
        start=0
        end=n-1
        it=int((n-start)/2)
        for i in range(it):
            temp=s[start+i]
            s[start+i]=s[end-i]
            s[end-i]=temp
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        