class Solution:
    def numOfWays(self, N: int) -> int:
        MOD = 10**9 + 7
        valid = []
        for i in range(3):
          for j in range(3):
            if i != j:
              for k in range(3):
                if k != j:
                  valid.append((i, j, k))
        m = len(valid)
        n_valid = [[] for _ in range(m)]
        for i in range(m):
          for j in range(m):
            flag = True
            for k in range(3):
              if valid[i][k] == valid[j][k]:
                flag = False
                break
            if flag:
              n_valid[i].append(j)
        @cache
        def dp(idx, prev):
          if idx == N:
            return 1
          total = 0
          for nxt in n_valid[prev]:
            total += dp(idx + 1, nxt)
          return total % MOD
        
        res = 0
        for i in range(m):
          res += dp(1, i)
        return res % MOD