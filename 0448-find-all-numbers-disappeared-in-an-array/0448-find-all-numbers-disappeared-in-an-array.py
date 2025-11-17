class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
          idx = abs(num) - 1
          if nums[idx] > 0:
            nums[idx] *= -1
        res = []
        for ind, val in enumerate(nums):
          if val > 0:
            res.append(ind + 1)
        return res 