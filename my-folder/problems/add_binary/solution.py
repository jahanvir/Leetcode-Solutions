class Solution(object):
    def addBinary(self, a, b):
        res=bin(int(a,2)+int(b,2))
        return res[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        