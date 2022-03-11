class Solution(object):
    def climbStairs(self, n):
        prev=0
        current=1
        for i in range(n):
            prev,current=current,prev+current
        return current
            
        """
        :type n: int
        :rtype: int
        """
        