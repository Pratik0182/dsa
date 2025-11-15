class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        N = len(nums) // 2
        for idx, val in enumerate(nums[:N]):
          res.append(val)
          res.append(nums[idx + N])
        return res