class Solution:
    def maxBottlesDrunk(self, nB: int, nE: int) -> int:
        res = nB
        while nB >= nE:
          curr = 0
          while nB >= nE:
            nB -= nE
            curr += 1
            nE += 1
          nB += curr
          res += curr
        return res