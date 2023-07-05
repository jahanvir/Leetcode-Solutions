class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l1=0
        l2=0
        maxl=0
        for n in nums:
            if n==1:
                l2+=1
            else:
                maxl=max(maxl,l1+l2)
                l1=l2
                l2=0
        maxl=max(maxl,l1+l2)
        return maxl-1 if maxl==len(nums) else maxl