class Solution(object):
    def divideString(self, s, k, fill):
        res = []
        N = len(s)
        for i in range(0, N, k):
            if i + k >= N:
                curr = s[i::] + (i + k - N) * fill
                res.append(curr)
            else:
                res.append(s[i:i + k])
        return res