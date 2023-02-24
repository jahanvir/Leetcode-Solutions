class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap, heapMax=[],0

        for n in nums:
            tmp=n
            while n%2==0:
                n=n//2
            heap.append((n,max(tmp,2*n)))
            heapMax= max(heapMax,n)
        #print(nums)
        #print(heap)

        res= float("inf")
        heapq.heapify(heap)
        while len(heap) == len(nums):
            n,nMax=heapq.heappop(heap)
            res=min(res,heapMax-n)

            if n<nMax:
                heapq.heappush(heap,(n*2,nMax))
                heapMax=max(heapMax,n*2)
            #print(heap)
        return res