class Solution(object):
    def maxSubArray(self, nums):
        
        maxsum=float("-inf")
        csum=float("-inf")
        for n in nums:
            csum=max(n,csum+n)
            maxsum=max(csum,maxsum)
        return maxsum
        
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        