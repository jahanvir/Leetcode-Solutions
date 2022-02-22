class Solution(object):
    def findNumbers(self, nums):
        count=0
        str_nums=map(str,nums)
        for s in str_nums:
            if len(s)%2==0:count+=1
        return count
            
        """
        :type nums: List[int]
        :rtype: int
        """
        