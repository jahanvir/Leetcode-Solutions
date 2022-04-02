class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if left==right and nums[0]==target:
            return left   
        while left<=right:
            pivot=left+(right-left)//2
            if nums[pivot]==target:
                return pivot
            if target<nums[pivot]:
                right=pivot-1
            else:
                left=pivot+1
        return -1
            
            
        