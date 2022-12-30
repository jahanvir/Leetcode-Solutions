class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        for n in nums:
            total+=n
        sumleft=0
        for i in range(len(nums)):          
            if sumleft==total-sumleft-nums[i]:
                return i
            sumleft+=nums[i]
        return -1
            
