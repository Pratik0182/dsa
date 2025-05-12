class Solution(object):
    def maxFreqSum(self, s):
        vow = (['a', 'e', 'i', 'o', 'u'])
        vc = defaultdict(int)
        cc = defaultdict(int)
        for ch in s:
            if ch in vow:
                vc[ch] += 1
            else:
                cc[ch] += 1
        vc[';'] = 0
        cc[';'] = 0
        return max(vc.values()) + max(cc.values())