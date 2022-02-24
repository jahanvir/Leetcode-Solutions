class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res=0
        for i in range(0,len(nums),2):
            res+=nums[i]
        return res
            
        """
        :type nums: List[int]
        :rtype: int
        """
        