class Solution(object):
    def heightChecker(self, heights):
        return sum(h1 != h2 for h1,h2 in zip(heights,sorted(heights)))
        """
        :type heights: List[int]
        :rtype: int
        """
        