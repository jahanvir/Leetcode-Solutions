class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp={}
        mod=10**9+7
        def dfs(l):
            if l>high:
                return 0
            if l in dp:
                return dp[l]
            dp[l]=1 if l>=low else 0
            dp[l]+=dfs(l+zero)+dfs(l+one)
            return dp[l] % mod
        
        return dfs(0)