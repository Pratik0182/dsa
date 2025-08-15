class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
          return False
        l, r = 0, 16
        while l < r:
          mid = (l + r) // 2
          if 4**mid < n:
            l = mid + 1
          else:
            r = mid
        return 4**l == n