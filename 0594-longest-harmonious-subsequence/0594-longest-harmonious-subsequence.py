from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        data = Counter(nums)
        res = 0
        for val in data:
            curr = data.get(val)
            x = max(data.get(val - 1, -curr), data.get(val + 1, -curr))
            res = max(res, curr + x)
        return res