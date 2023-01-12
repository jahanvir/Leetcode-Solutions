class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans=[1]*n
        mapper=defaultdict(list)
        for edge in edges:
            f,t=edge
            mapper[f].append(t)
            mapper[t].append(f)
        
        def dfs(node, last, mapper,labels,ans):
            counter=collections.Counter()
            for subt in mapper[node]:
                if subt==last:
                    continue
                counter+=dfs(subt,node,mapper,labels, ans)
            counter[labels[node]]+=1
            ans[node]=counter[labels[node]]
            return counter

        dfs(0,-1,mapper,labels, ans)
        return ans