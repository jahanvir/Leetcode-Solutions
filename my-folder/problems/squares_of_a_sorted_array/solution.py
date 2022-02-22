class Solution(object):
    def sortedSquares(self, nums):
        sqr_num=[n*n for n in nums]
        return sorted(sqr_num)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        