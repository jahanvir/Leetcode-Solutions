class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        kmod=1000000007
        l=0
        r=len(nums)-1
        ans=0
        while l<=r:
            if nums[l]+nums[r]<=target:
                ans+=pow(2,r-l,kmod)
                l+=1
            else:
                r-=1
        return ans%kmod
