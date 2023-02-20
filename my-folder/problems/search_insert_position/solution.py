class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n=len(nums)
        i=0
        j=n-1
        mid=n//2
        while i <= j:
            mid = (i+j)//2
            if target < nums[mid]:
                j=mid-1
            elif target > nums[mid]:
                i=mid+1
            else:
                return mid
            
        return j+1

