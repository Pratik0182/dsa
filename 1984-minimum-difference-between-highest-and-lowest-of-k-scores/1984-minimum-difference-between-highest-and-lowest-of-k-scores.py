class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
      if k == 1:
        return 0
  
      nums.sort()
      res = float('inf')
      i = 0
      j = k - 1
      print(nums)
      while j < len(nums):
        res = min(res, nums[j] - nums[i])
        i += 1
        j += 1
      return res