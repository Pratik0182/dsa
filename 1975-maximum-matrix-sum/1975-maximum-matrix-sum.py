class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        data = []
        for r in matrix:
          for v in r:
            data.append(v)
        data.sort()
        N = len(data)
        for i in range(0, N - 1, 2):
          if -1 * (data[i] + data[i + 1]) > data[i] + data[i + 1]:
            data[i] *= -1
            data[i + 1] *= -1
        return sum(data)
