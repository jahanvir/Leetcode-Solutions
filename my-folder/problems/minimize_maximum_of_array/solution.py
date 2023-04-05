class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        ans=nums[0]
        total=0

        for i,n in enumerate(nums):
            total+=n
            res=math.ceil(total/(i+1))
            if res > ans:
                ans=res
        return ans
