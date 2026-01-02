class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        N = len(nums) // 2
        for num in nums:
          hm[num] += 1
          if hm[num] == N:
            return num
        