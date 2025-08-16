class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x, x + k // 2):
          N = i - x
          for j in range(y, y + k):
            grid[i][j], grid[x + k - 1 - N][j] = grid[x + k - 1 - N][j], grid[i][j]
        return grid