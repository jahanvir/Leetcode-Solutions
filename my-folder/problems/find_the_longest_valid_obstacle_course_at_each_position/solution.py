class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        ans=[]
        dp=[10**8 for _ in range(len(obstacles)+1)]

        for o in obstacles:
            index=bisect.bisect(dp,o)
            ans.append(index+1)
            dp[index]=o
        
        return ans
        