class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        temp = {val : idx for idx, val in enumerate(temp)}
        C = Counter(nums)
        res = []
        for num in nums:
          res.append(temp[num] - (C[num] - 1))
        return res