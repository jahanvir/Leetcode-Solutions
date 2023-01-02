class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        def allSmall(word):
            for w in word:
                if not (ord(w) >=ord('a') and ord(w)<=ord('z')):
                    return False
            return True
        
        def allCaps(word):
            for w in word:
                if not (ord(w) >=ord('A') and ord(w)<=ord('Z')):
                    return False
            return True        
        
        c=word[0]
        if ord(c) >=ord('a') and ord(c)<=ord('z'):
            return allSmall(word)
        if len(word)==1:
            return True
        c=word[1]
        if ord(c) >=ord('A') and ord(c)<=ord('Z'):
            return allCaps(word)
        return allSmall(word[1:])



        
    