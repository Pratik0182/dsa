class Solution:
    def minOperations(self, nums: List[int]) -> int:
      data = [-1]
      res = 0
      for num in nums:
        while num < data[-1]:
          data.pop()
        if num > data[-1]:
          res += (num > 0)
          data.append(num)
      return res