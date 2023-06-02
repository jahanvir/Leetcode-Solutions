class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int: 
        # preprocessing
        n=len(bombs)
        brange=[[] for _ in range(n)]
    
        
        for i,(xi,yi,ri) in enumerate(bombs):
            for j,(xj,yj,rj) in enumerate(bombs):
                if i==j:
                    continue
                if ri**2>=(xi-xj)**2 + (yi-yj)**2:
                    brange[i].append(j)
        
        def dfs(bomb,detonated):
            for r in brange[bomb]:
                if r in detonated:
                    continue
                detonated.add(r)
                dfs(r,detonated)
        ans=0
        for i in range(n):
            detonated=set([i])
            dfs(i,detonated)
            ans=max(ans,len(detonated))
        
        return ans
            

             
                
        
