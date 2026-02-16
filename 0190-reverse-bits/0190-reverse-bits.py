class Solution:
    def reverseBits(self, n: int) -> int:
        def int_to_bin(intt):
          res = []
          while intt > 0:
            res.append(str(intt % 2))
            intt //= 2
          return "".join(reversed(res)).zfill(32)

        def bin_to_int(bina):
          res = 0
          for idx, val in enumerate(reversed(bina)):
            res += int(val) * 2**(idx)
          return res
        
        return bin_to_int(int_to_bin(n)[::-1])