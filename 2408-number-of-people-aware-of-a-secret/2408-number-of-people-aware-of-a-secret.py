class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1 
        MOD = 10**9 + 7
        for i in range(1, n + 1):
          for j in range(i + delay, min(n + 1, i + forget)):
            dp[j] = (dp[j] + dp[i]) % MOD

        res = 0
        for i in range(n - forget + 1, n + 1):
          res = (res + dp[i]) % MOD
        return res