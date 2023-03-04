class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        j=-1
        prevMin=-1
        prevMax=-1

        for i,num in enumerate(nums):
            if num<minK or num>maxK:
                j=i
            if num==minK:
                prevMin=i
            if num==maxK:
                prevMax=i
            ans+=max(0,min(prevMin,prevMax)-j)
        return ans