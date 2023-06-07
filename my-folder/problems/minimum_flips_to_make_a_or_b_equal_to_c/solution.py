class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
      ans1=((a | b) ^ c)
      ans2=a & b & ans1
      return ans1.bit_count() + ans2.bit_count()