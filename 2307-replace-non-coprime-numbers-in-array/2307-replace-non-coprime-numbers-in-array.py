class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)
        res = []
        for i in range(len(nums)):
            res.append(nums[i])
            while len(res) >= 2 and gcd(res[-1], res[-2]) > 1:
                    LCM = (res[-1] * res[-2]) // gcd(res[-1], res[-2])
                    res.pop()
                    res.pop()
                    res.append(LCM)
        return res