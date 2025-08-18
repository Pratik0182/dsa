class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
      if k - 1 + maxPts <= n:
        return 1.0
      dp = [0.0] * (k + maxPts)
      for i in range(k, k + maxPts):
        if i <= n:
          dp[i] = 1.0
        else:
          dp[i] = 0.0
      #if start from k - 1 -> v(k) + v(k + 1) .. v(k - 1 + max)
      res = sum(dp[i] for i in range(k, k + maxPts))
      for i in range(k - 1, -1, -1):
        dp[i] = res / maxPts
        res += dp[i]
        res -= dp[i + maxPts]
      return dp[0]