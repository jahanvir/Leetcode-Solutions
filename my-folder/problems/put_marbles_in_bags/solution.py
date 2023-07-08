class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pairs=[]
        n=len(weights)
        for i in range(0,n-1):
            pairs.append(weights[i]+weights[i+1])
        
        return sum(heapq.nlargest(k-1,pairs))-sum(heapq.nsmallest(k-1,pairs))

