class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[0]*(len(nums2)+1)

        for i in range(len(nums1)):
            currDP=[0]*(len(nums2)+1)
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    currDP[j+1]=1+dp[j]
                else:
                    currDP[j+1]=max(dp[j+1],currDP[j])
                
            dp=currDP
                
        return dp[len(nums2)]
        