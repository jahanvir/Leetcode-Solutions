class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        visit=set((0,0))
        q=deque([(0,0,1)])
        N=len(grid)
        dir=[[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]

        while q:
            r,c,length=q.popleft()
            if (min(r,c)<0 or max(r,c)>=N or grid[r][c]):
                continue
            if r==N-1 and c==N-1:
                return length
            
            for dr,dc in dir:
                if (r+dr,c+dc) not in visit:
                    q.append((r+dr,c+dc,length+1))
                    visit.add((r+dr,c+dc))
        return -1
