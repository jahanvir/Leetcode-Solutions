class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        n=len(nums)
        avg=2*k+1
        ans=[-1]*n
        if avg>n:
            return ans
        ans[k]=sum(nums[:avg])
        for i in range(k+1,n-k):
            ans[i]=ans[i-1]-nums[i-k-1]+nums[i+k]
        print(ans)
        for i in range(k,n-k):
            ans[i]=ans[i]//avg
        return ans

