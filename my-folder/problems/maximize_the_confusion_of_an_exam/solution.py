class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        count=collections.Counter(answerKey[:k])
        ans=k
        for right in range(k,len(answerKey)):
            count[answerKey[right]]+=1
            
            while min(count['T'],count['F'])>k:
                count[answerKey[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
        