class Solution(object):
    def minSum(self, nums1, nums2):
        Z1, Z2 = nums1.count(0), nums2.count(0)
        S1, S2 = sum(nums1), sum(nums2)
        if Z1 == 0 and Z2 == 0:
            return S1 if S1 == S2 else -1
        if Z1 == 0:
            return -1 if S1 < S2 + Z2 else S1
        if Z2 == 0:
            return -1 if S2 < S1 + Z1 else S2
        return max(S1 + Z1, S2 + Z2)