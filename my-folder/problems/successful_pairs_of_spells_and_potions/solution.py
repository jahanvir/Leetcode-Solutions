class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def successIndex(spell):
            l=0
            r=len(potions)

            while l<r:
                m = (l+r)//2
                if spell * potions[m]>=success:
                    r=m
                else:
                    l=m+1
            return l

        return [len(potions)-successIndex(spell) for spell in spells]
        