class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        #j -> 2, 5
        ## |x - j| <= k
        data = []
        for idx, num in enumerate(nums):
          if num == key:
            data.append(idx)
        res = []
        for i in range(len(nums)):
          idx = bisect.bisect(data, i)
          near = float('inf')
          if idx < len(data):
            near = min(near, abs(data[idx] - i))
          if idx > 0:
            near = min(near, abs(data[idx - 1] - i))
          if near <= k:
            res.append(i)
        return res