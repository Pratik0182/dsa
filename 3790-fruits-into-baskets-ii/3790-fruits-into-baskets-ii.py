class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
      res = len(fruits)
      seen = [False] * len(baskets)
      for f in fruits:
        for idx, val in enumerate(baskets):
          if val >= f and not seen[idx]:
            seen[idx] = True
            res -= 1
            break
      return res