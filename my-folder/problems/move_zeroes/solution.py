class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        i,items=0,0
        while i<n and items<=n:
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
                i-=1
            i+=1
            items+=1
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        