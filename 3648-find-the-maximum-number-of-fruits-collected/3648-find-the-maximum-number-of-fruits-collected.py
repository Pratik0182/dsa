class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
      N = len(fruits)
      dpu = [[float('-inf')] * N for _ in range(N)] #(0, n - 1)
      dpl = [[float('-inf')] * N for _ in range(N)] #(n - 1, 0)
      dec = int(ceil(N / 2)) - 1
      cond = lambda i, j: 0 <= i < N and 0 <= j < N
      for i in range(N - (1 - N % 2)):
        for j in range(abs(i - dec) + (N - 1 - dec), N):
          if i == j:
            continue
          #UPPER HALF
          v1 = dpu[i - 1][j + 1] if cond(i - 1, j + 1) else 0
          v2 = dpu[i - 1][j] if cond(i - 1, j) else 0
          v3 = dpu[i - 1][j - 1] if cond(i - 1, j - 1) else 0
          dpu[i][j] = fruits[i][j] + max(v1, v2, v3, 0)
          #LOWER HALF
          v1 = dpl[j + 1][i - 1] if cond(j + 1, i - 1) else 0
          v2 = dpl[j][i - 1] if cond(j, i - 1) else 0
          v3 = dpl[j - 1][i - 1] if cond(j - 1, i - 1) else 0
          dpl[j][i] = fruits[j][i] + max(v1, v2, v3, 0)
      res = sum(fruits[i][i] for i in range(N)) + max(map(max, dpu)) + max(map(max, dpl))
      return res