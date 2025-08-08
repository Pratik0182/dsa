class Solution:
    def soupServings(self, N: int) -> float:
      if N >= 4500: return 1.0
      N = ceil(N / 25)
      @cache
      def help(a, b):
        if a <= 0 and b <= 0:
          return 0.5
        if a <= 0:
          return 1.0
        if b <= 0:
          return 0
        op1 = help(a - 4, b)
        op2 = help(a - 3, b - 1)
        op3 = help(a - 2, b - 2)
        op4 = help(a - 1, b - 3)
        return sum([op1, op2, op3, op4]) * 0.25
      return help(N, N)