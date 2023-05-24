class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=[(a,b) for a,b in zip(nums1,nums2)]
        pairs=sorted(pairs, key=lambda p: p[1], reverse=True)

        minHeap=[]
        n1sum=0
        res=0
        print(pairs)
        for n1,n2 in pairs:
            n1sum+=n1
            heapq.heappush(minHeap,n1)
            if len(minHeap) > k:
                n1pop=heapq.heappop(minHeap)
                n1sum-=n1pop

            if len(minHeap) == k:
                res = max(res,n1sum*n2)
        return res                