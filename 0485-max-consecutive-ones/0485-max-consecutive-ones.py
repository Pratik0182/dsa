class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for val in nums:
          if val == 1:
            curr += 1
          else:
            res = max(res, curr)
            curr = 0
        return max(res, curr)