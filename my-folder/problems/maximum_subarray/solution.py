class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=min(nums)
        currSum=0
        for n in nums:
            currSum=max(n,n+currSum)
            maxSum=max(maxSum,currSum)
        return maxSum

        
        