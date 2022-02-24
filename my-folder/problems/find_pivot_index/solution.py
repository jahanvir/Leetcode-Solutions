class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        if sum(nums[1:])==0:return 0
        for i in range(1,n-1):
            if sum(nums[:i])==sum(nums[i+1:]):
                return index(i)
        if sum(nums[:n-1])==0:return n-1
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        