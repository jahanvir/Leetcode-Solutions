class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        N = len(strs)
        dsu= DSU(N)
        for i in range(N):
            for j in range(i+1,N):
                if self.isSimilar(strs[i],strs[j]):
                    dsu.union(i,j)
        return dsu.regions()

    def isSimilar(self,str1,str2):
        count=0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count+=1
        return count==2 or count==0
        
class DSU:
    def __init__(self,N):
        self.par_ = list(range(N+1))
        self.regions_ = N
    
    def find(self,x):
        if x != self.par_[x]:
            self.par_[x] = self.find(self.par_[x])
        return self.par_[x]
    
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)

        if px == py:
            return 
        self.par_[px] = py
        self.regions_ -=1
    
    def regions(self):
        return self.regions_
        
