class Solution(object):
    def reverseWords(self, s):
        temp=s.split()
        for i in range(len(temp)):
            temp[i]=temp[i][::-1]
        return " ".join(temp)
            
        """
        :type s: str
        :rtype: str
        """
        