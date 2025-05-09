class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        N = len(num)
        fact = [1]
        factI = [pow(1, -1, MOD)]
        freq = [0] * 10
        for v in num:
            freq[int(v)] += 1
        for i in range(1, N + 1):
            fact.append((fact[-1] * i) % MOD)
            factI.append(pow(fact[-1], -1, MOD))
        numer = (fact[(N + 1) // 2] * fact[N // 2]) % MOD if N % 2 == 1 else \
                (fact[N // 2] * fact[N // 2]) % MOD
        @cache
        def helper(idx, S, C):
            if idx == 10:
                if S != 0:
                    return 0
                if N % 2 == 0:
                    return 1 if C == 0 else 0
                else:
                    return 1 if C == 1 else 0
            res = 0
            for i in range(freq[idx] + 1):
                odd = i
                even = freq[idx] - i
                res += helper(idx + 1, S + (odd - even) * idx, C + (odd - even)) * factI[odd] * factI[even]
                res %= MOD
            return res % MOD
        return (helper(0, 0, 0) * numer) % MOD