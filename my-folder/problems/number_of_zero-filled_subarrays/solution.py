class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans=0
        nonZeroIndex=-1

        for i,num in enumerate(nums):

            if num:
                nonZeroIndex=i
            else:
                ans+=i-nonZeroIndex
        return ans