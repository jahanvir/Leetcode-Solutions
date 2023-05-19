class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        col=[0]*len(graph)
        def bfs(i):
            if col[i]:
                return True
            
            q=deque([i])
            col[i]= -1 

            while q:
                v = q.popleft()
                for nei in graph[v]:
                    if col[nei] and col[nei]==col[v]:
                        return False
                    elif not col[nei]:
                        q.append(nei)
                        col[nei]=-1*col[v]
            return True
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True