class Solution(object):
    def containsDuplicate(self, nums):
        res=set()
        for n in nums:
            if n in res:
                return True
            res.add(n)
        """
        :type nums: List[int]
        :rtype: bool
        """
        