class Solution(object):
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        d = {'c' : set(), 'di' : set(), 'adi' : set()}
        def helper(R):
            if R == n:
                res.append(["".join(V) for V in board])
                return 
            for C in range(n):
                if C not in d['c'] and R - C not in d['di'] and R + C not in d['adi']:
                    d['c'].add(C)
                    d['di'].add(R - C)
                    d['adi'].add(R + C)
                    board[R][C] = 'Q'
                    helper(R + 1)
                    d['c'].remove(C)
                    d['di'].remove(R - C)
                    d['adi'].remove(R + C)
                    board[R][C] = '.'
        helper(0)
        return res