class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]+=1
        for i,c in count.items():
            freq[c].append(i)
        
        ans=[]
        for f in range(len(freq)-1,0,-1):
            for i in freq[f]:
                ans.append(i)
                if len(ans)==k:
                    return ans
        

        