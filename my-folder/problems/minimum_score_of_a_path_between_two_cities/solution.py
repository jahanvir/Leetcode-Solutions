class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
            ans=math.inf
            graphs=[[] for _ in range(n+1)]
            q=collections.deque([1])
            seen={1}

            for u,v,distance in roads:
                graphs[u].append((v,distance))
                graphs[v].append((u,distance))

            while q:
                u=q.popleft()
                for v,d in graphs[u]:
                    ans=min(ans,d)
                    if v in seen:
                        continue
                    q.append(v)
                    seen.add(v)
            return ans



        