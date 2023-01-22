class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        n=len(nums)
        for i in range(len(nums)):
            nums[i]+=n * (nums[nums[i]]%n)
        
    
        for i in range(len(nums)):
            nums[i]=nums[i]//n
        return nums