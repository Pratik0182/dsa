class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 2**(r - l)
                l += 1
            else:
                r -= 1
        return res % MOD