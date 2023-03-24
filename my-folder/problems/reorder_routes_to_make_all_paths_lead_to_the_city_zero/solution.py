class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        edges={(a,b) for a,b in connections}
        neighbors = {city :[] for city in range(n)}

        visit=set()
        ans=0

        for a,b in connections:
           neighbors[a].append(b)
           neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, ans

            for nb in neighbors[city]:
                if nb in visit:
                    continue
                if (nb,city) not in edges:
                    ans+=1
                visit.add(nb)
                dfs(nb)

        visit.add(0)
        dfs(0)
        return ans