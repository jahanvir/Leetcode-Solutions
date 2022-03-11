class Solution:
    def romanToInt(self, s: str) -> int:
    
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot=0
        prev='I'
    
        for i in s[::-1]:
            if rom[i]<rom[prev]:
                tot=tot-rom[i]
            else:
                tot=tot+rom[i]
            prev=i
            
                
            
        return tot
        