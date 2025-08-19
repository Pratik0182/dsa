class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
      N = len(nums)
      dp = [0] * N
      dp[0] = int(nums[0] == 0)
      for i in range(1, N):
        if nums[i] == 0:
          dp[i] = 1 + dp[i - 1]
      return sum(dp)