class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calCost(val):
            return sum(abs(val-num)*c for num,c in zip(nums,cost))
        
        left=min(nums)
        right=max(nums)  
        ans=calCost(nums[0])
        # ans2=nums[0]

        while left < right:
            mid=(left+right)//2
            cost1=calCost(mid)
            cost2=calCost(mid+1)
            ans=min(cost1,cost2)
            # ans2=mid if cost1<cost2 else mid+1
            if cost1>cost2:
                left=mid+1
            else:
                right=mid
        # print(ans2)
        return ans

        