class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        MOD = 10**9 + 7
        while n > 0:
          val = int(log2(n))
          powers.append(2**val)
          n -= 2**val
        
        powers = powers[::-1]
        PF = [powers[0]]
        for i in range(1, len(powers)):
          PF.append((powers[i] * PF[i - 1]) % MOD)
        
        res = []
        for l, r in queries:
          if l == 0:
            res.append(PF[r])
          else:
            res.append((PF[r] * pow(PF[l - 1], MOD - 2, MOD)) % MOD)
        return res