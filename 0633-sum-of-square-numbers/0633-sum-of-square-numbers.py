class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            v1 = a**2
            v2 = int((c - v1)**0.5)**2
            if v1 + v2 == c:
                return True
        return False