class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        N = []
        ssum = 0
        for c in str(n):
            if c != '0':
                N.append(c)
                ssum += int(c)
        N = int("".join(N))
        return N * ssum