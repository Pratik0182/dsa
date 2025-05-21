class Solution(object):
    def setZeroes(self, matrix):
        M, N = len(matrix), len(matrix[0])
        R0 = any(matrix[0][i] == 0 for i in range(N))
        C0 = any(matrix[i][0] == 0 for i in range(M))
        for r in range(1, M):
            for c in range(1, N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, M):
            for c in range(1, N):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if R0:
            for c in range(N):
                matrix[0][c] = 0
        if C0:
            for r in range(M):
                matrix[r][0] = 0
