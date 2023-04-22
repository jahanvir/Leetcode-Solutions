class Solution:
    def minInsertions(self, s: str) -> int:

        def findMaxPalinSubSeq(s:str):

            n=len(s)
            dp=[[0]*n for _ in range(n)]

            for i in range(n):
                dp[i][i]=1
            
            for w in range(1,n):
                for i in range(n-w):
                    j=i+w

                    if s[i]==s[j]:
                        dp[i][j]=dp[i+1][j-1]+2
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
            return dp[0][n-1]
        
        return len(s)-findMaxPalinSubSeq(s)