class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1   
                # print(right,left,dp)
            
        
        return max(dp.values())