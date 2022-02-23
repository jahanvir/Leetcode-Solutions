class Solution(object):
    def sortArrayByParity(self, nums):
        return [n for n in nums if not n%2]+[n for n in nums if n%2]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        