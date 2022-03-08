class Solution(object):
    def reverse(self, x):
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=int("-"+str(x)[::-1][:-1])
        return -2**31<=x<=2**31 and x or 0
        """
        :type x: int
        :rtype: int
        """
        