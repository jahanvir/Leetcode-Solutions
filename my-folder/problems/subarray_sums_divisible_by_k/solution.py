class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        map=[0]*k
        total=0
        count=0
        map[0]=1
        for n in nums:
            total= (total+n)%k
            count+=map[total]
            map[total]+=1
        return count


        