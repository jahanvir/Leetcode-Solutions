class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        r=len(grid)
        c=len(grid[0])
        count=1
        start=[0,0]
        self.roots=0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    start[0]=i
                    start[1]=j
                elif grid[i][j]==0:
                    count+=1

        def valid(i,j,count):
            if not (0 <= i < r and 0<=j<c):
                return 
            if grid[i][j]<0:
                return
            if grid[i][j]==2:
                if count==0:
                    self.roots+=1
                return 
            grid[i][j]=-2
            valid(i+1,j,count-1)
            valid(i-1,j,count-1)
            valid(i,j+1,count-1)
            valid(i,j-1,count-1)
            grid[i][j]=0
        
        valid(start[0],start[1],count)
        return self.roots
       



