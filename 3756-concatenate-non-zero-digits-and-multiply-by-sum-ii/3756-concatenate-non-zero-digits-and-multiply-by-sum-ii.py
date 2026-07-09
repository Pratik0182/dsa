class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        MOD = 10 ** 9 + 7
        pf, x, nz = [0], [0], [0]
        for c in s:
            pf.append((pf[-1] + int(c)) % MOD)
            if c == '0':
                nz.append(nz[-1] + 1)
                x.append(x[-1])
            else:
                nz.append(nz[-1])
                x.append((x[-1] * 10 + int(c)) % MOD)
        res = []
        for l, r in queries:
            ssum = pf[r + 1] - pf[l]
            digits = r - l + 1 - (nz[r + 1] - nz[l])
            v = x[r + 1] - x[l] * pow(10, digits, MOD)
            res.append((v * ssum) % MOD)
        return res