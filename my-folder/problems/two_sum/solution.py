class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        