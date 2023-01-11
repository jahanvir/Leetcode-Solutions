class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.mapp=defaultdict(list)
        for edge in edges:
            f,t=edge
            self.mapp[f].append(t)
            self.mapp[t].append(f)
        visited=set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            res=0
            for child in self.mapp[node]:
                res+=dfs(child)
            
            if node!=0 and (res>0 or hasApple[node]):
                res+=2
            return res
        return dfs(0)
            