class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        d=disjointSet(n)
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    d.union(i,j)
        count=0
        for i in range(n):
            if d.find(i)==i:
                count+=1
        return count
                    
        
class disjointSet(object):
    def __init__(self,length):
        self.root=[i for i in range(length)]
        self.rank=[1]*length
    def find(self,x):
        if self.root[x]==x:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rooty]>self.rank[rootx]:
                self.root[rootx]=rooty
            else:
                self.root[rootx]=rooty
                self.rank[rooty]+=1
    def connected(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        return rootx==rooty
            
        
        
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        