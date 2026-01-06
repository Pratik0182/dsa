class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        N = max(nums)
        S = {i: [] for i in range(1, N + 1)}
        for i in range(1, N + 1):
          j = i
          while j <= N:
             S[j].append(i)
             j += i
        res = 0
        for i in nums:
          if len(S[i]) == 4:
            res += sum(S[i])
        return res
