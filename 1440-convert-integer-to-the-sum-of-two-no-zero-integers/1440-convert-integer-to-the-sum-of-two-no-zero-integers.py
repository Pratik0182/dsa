class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
      def isvalid(a, b):
        for v1 in str(a):
          if v1 == '0':
            return False
        for v2 in str(b):
          if v2 == '0':
            return False
        return True
      for i in range(n, 0, -1):
        if isvalid(i, n - i):
          return [i, n - i]