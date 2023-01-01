class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match=s.split()
        mapper={}
        mapped=set()
        
        if len(match) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapper:
                if mapper[pattern[i]] != match[i]:
                    return False
            else:
                if match[i] in mapped:
                    return False
                mapper[pattern[i]]=match[i]
                mapped.add(match[i])
        return True

