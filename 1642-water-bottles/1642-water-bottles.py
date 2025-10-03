class Solution:
    def numWaterBottles(self, nB: int, nE: int) -> int:
        res = nB
        while nB >= nE:
          res += nB // nE
          nB = nB // nE + nB % nE
        return res