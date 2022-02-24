class Solution(object):
    def rotate(self, nums, k):
        n=k%len(nums)
        nums[:]=nums[-n:]+nums[:-n]
        
        
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        