class Solution:
    def compress(self, chars: List[str]) -> int:

        ans=0
        n=len(chars)
        i=0
        while i<n:
            prev=chars[i]
            count=0
            while i<n and chars[i]==prev:
                count+=1
                i+=1
            chars[ans]=prev
            ans+=1
            if count>1:
                for c in str(count):
                    chars[ans]=c
                    ans+=1
        return ans
            

