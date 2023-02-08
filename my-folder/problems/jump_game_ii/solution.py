class Solution:
    def jump(self, nums: List[int]) -> int:

        n=len(nums)
        far=0
        cur_end=0
        ans=0
        for i in range(n-1):
            far=max(far,i+nums[i])

            if i==cur_end:
                ans+=1
                cur_end=far
        return ans


