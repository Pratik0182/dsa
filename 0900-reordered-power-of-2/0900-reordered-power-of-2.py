class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        data = Counter(str(n))
        N = int(log10(n)) + 1
        i = 0
        while 2**i < 10**N:
          if Counter(str(2**i)) == data:
            return True
          i += 1
        return False