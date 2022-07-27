class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    
        total=0
        for n in nums:
            total+=n
        total_left=0
        for i in range(len(nums)):
            if total_left==(total-nums[i]-total_left):
                return i
            total_left+=nums[i]
        return -1
            
            
        