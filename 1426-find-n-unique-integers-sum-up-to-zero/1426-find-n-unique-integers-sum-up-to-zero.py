class Solution:
    def sumZero(self, n: int) -> List[int]:
        ##Odd
        res = []
        if n & 1:
          for i in range(-(n // 2), n // 2 + 1):
            res.append(i)
        else:
          for i in range(-(n // 2), n // 2 + 1):
            if i == 0:
              continue
            res.append(i)
        return res