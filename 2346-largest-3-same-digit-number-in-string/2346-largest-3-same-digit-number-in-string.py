class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = float('-inf')
        for i in range(len(num) - 3 + 1):
          curr = num[i : i + 3]
          if len(set(curr)) == 1:
            res = max(res, int(curr))
        return str(res).zfill(3) if res != float('-inf') else ""