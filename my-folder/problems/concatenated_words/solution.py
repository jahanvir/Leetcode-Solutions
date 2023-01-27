class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mem={}
        mappedwords=set(words)
        def check(word):
            if len(word)==1:
                return False
            if word in mem:
                return mem[word]
            mem[word]=False
            for i in range(1,len(word)):
                prefix,suffix=word[:i],word[i:]
                if prefix in mappedwords and (suffix in mappedwords or check(suffix)):
                    mem[word]=True
                    break
            return mem[word]

        return [w for w in words if check(w)]
