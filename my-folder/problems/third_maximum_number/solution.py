class Solution(object):
    def thirdMax(self, nums):
        res=list(set(nums))
        res.sort()
        if len(res)<3:return res[-1]
        return res[len(res)-3]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        