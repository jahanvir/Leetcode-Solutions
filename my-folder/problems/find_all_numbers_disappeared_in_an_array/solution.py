class Solution(object):
    def findDisappearedNumbers(self, nums):
        res=set(nums)
        temp=set(range(1,len(nums)+1))
        return temp-res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        