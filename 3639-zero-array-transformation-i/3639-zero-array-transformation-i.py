class Solution(object):
    def isZeroArray(self, nums, queries):
        memo = defaultdict(int)
        curr = 0
        for l, r in queries:
            memo[l] += 1
            memo[r + 1] -= 1
        for idx, val in enumerate(nums):
            curr += memo.get(idx, 0)
            if curr < val:
                return False
        return True