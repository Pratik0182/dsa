class Solution:
    def minimumCost(self, nums: List[int]) -> int:
      sec = float('inf')
      third = float('inf')
      for v in nums[1:]:
        if v <= sec:
          third, sec = sec, v
        elif v < third:
          third = v
      
      return nums[0] + sec + third