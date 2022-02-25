class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        d=DisjointSet(len(s))
        res=[]
        m=collections.defaultdict(list)
        
        for x,y in pairs:
            d.union(x,y)
        for i in range(len(s)):
            m[d.find(i)].append(s[i])
        for comp in m.keys():
            m[comp].sort(reverse=True)
        for i in range(len(s)):
            res.append(m[d.find(i)].pop())
        return "".join(res)
        
        
        
        
#dijoint set 
class DisjointSet(object):
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
            if self.rank[rootx]> self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.root[rootx]=rooty
            else:
                self.root[rootx]=rooty
                self.rank[rooty]+=1
    def connected(self,x,y):
        return self.find(x)==self.find(y)
        

        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        