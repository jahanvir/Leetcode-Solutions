class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)-1
        n=len(grid[0])
        ans=0
        i,j=m,0
        while i>=0 and j<n:
            if grid[i][j]<0:
                ans+=n-j
                i-=1
            else:
                j+=1
        return ans