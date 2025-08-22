class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
      M = len(grid)
      N = len(grid[0])
      minI, maxI = float('inf'), float('-inf')
      minJ, maxJ = float('inf'), float('-inf')
      for i in range(M):
        for j in range(N):
          if grid[i][j] == 1:
            #length
            minI = min(minI, i)
            maxI = max(maxI, i)

            #breadth
            minJ = min(minJ, j)
            maxJ = max(maxJ, j)
      return (maxI - minI + 1) * (maxJ - minJ + 1)