class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        letters=list(range(26))

        def find(x):
            if letters[x] != x:
                letters[x]=find(letters[x])
            return letters[x]
        
        for i in range(len(s1)):
            a,b=ord(s1[i])-ord('a'), ord(s2[i])-ord('a')
            pa,pb=find(a),find(b)
            if pa<pb:
                letters[pb]=pa
            else:
                letters[pa]=pb

        res=[]
        for ch in baseStr:
            temp=ord(ch)-ord('a') 
            res.append(chr(find(temp)+ord('a')))
        return ''.join(res)
