class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        l=0
        res=len(nums)+1
        cur=0
        for r,num in enumerate(nums):
            cur+=num
            while cur>=target:
                res=min(res,r-l+1)
                cur=cur-nums[l]
                l=l+1
        return res<len(nums)+1 and res or 0
            
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        