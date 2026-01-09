class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #i, j
        M, N = len(nums1), len(nums2)
        dp = [[float('-inf')] * N for _ in range(M)]
        for i in range(M):
          for j in range(N):
            new = nums1[i] * nums2[j]
            res = new
            if i > 0 and j > 0:
              res = max(res, new + dp[i - 1][j - 1])
            if i > 0:
              res = max(res, dp[i - 1][j])
            if j > 0:
              res = max(res, dp[i][j - 1])
            dp[i][j] = res
        
        return dp[M - 1][N - 1]
