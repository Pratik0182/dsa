class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        N = len(nums)
        data = sorted(((v ^ k) - v for v in nums), reverse = True)
        res = sum(nums)
        for i in range(1, N, 2):
            if data[i] + data[i - 1] > 0:
                res += data[i] + data[i - 1]
        return res
