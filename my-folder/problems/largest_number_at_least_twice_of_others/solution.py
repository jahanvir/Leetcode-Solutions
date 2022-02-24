class Solution(object):
    def dominantIndex(self, nums):
        big=max(nums)
        ind=nums.index(big)
        nums.pop(ind)
        for n in nums:
            if n==big or n*2>big:
                return -1
        return ind
        """
        :type nums: List[int]
        :rtype: int
        """
        