class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        check = [1] * (N + 1)
        res = []
        for num in nums:
          check[num] -= 1
          if check[num] == -1:
            res.append(num)
        for idx, val in enumerate(check):
          if val == 1 and idx != 0:
            res.append(idx)
            break
        return res