class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)

        def find(n):
            p=par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def union(n1,n2):
            pn1=find(n1)
            pn2=find(n2)

            if pn1==pn2:
                return False
            
            if rank[pn1] > rank[pn2]:
                par[pn2]=pn1
                rank[pn1]+=rank[pn2]
            else:
                par[pn1]=pn2
                rank[pn2]+=rank[pn1]
            return True
        
        for e in edges:
            if not union(e[0],e[1]):
                return e
