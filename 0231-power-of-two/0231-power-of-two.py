class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      if n <= 0: return False
      x = int(log2(n))
      return 2**x == n