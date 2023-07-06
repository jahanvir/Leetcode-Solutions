class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=len(nums)+1
        l=0
        preSum=0
        for r,n in enumerate(nums):
            preSum+=n
            while preSum>=target:
                ans=min(ans,r-l+1)
                preSum-=nums[l]
                l+=1
        return ans if ans!=len(nums)+1 else 0
