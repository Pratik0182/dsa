class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        res = 0
        hm = set(nums)
        if original not in hm:
          return original
        while original <= max(nums):
          if original in hm:
            original *= 2
          else:
            break
        return original