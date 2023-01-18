class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n=len(nums)
        sum=0
        
        if n==1:
            return nums[0]

        for num in nums:
            sum+=num

        maxSoFar=nums[0]
        minSoFar=nums[0]
        currMax=nums[0]
        currMin=nums[0]

        for i in range(1,n):

            currMax=max(currMax+nums[i], nums[i])
            maxSoFar=max(maxSoFar, currMax)

            currMin=min(currMin+nums[i],nums[i])
            minSoFar=min(minSoFar,currMin)

        if minSoFar==sum:
            return maxSoFar
        
        return(max(maxSoFar,sum-minSoFar))

