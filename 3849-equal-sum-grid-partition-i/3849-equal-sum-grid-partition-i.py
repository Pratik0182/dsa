class Solution(object):
    def canPartitionGrid(self, grid):
        M, N = len(grid), len(grid[0])
        rPS, cPS = [0] * M, [0] * N
        rPS[0], cPS[0] = sum(grid[0]), sum(grid[i][0] for i in range(M))
        for i in range(1, M):
            rPS[i] = rPS[i - 1] + sum(grid[i])
        for j in range(1, N):
            cPS[j] = cPS[j - 1] + sum(grid[x][j] for x in range(M))

        for i in range(M - 1):
            if rPS[i] == rPS[M - 1] - rPS[i]:
                return True

        for i in range(N - 1):
            if cPS[i] == cPS[N - 1] - cPS[i]:
                return True

        return False
        