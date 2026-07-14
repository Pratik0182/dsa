class Solution:
    def candy(self, r: List[int]) -> int:
        N = len(r)
        cy = [1] * N
        for i in range(1, N):
            if r[i] > r[i - 1]:
                cy[i] = cy[i - 1] + 1
        
        for i in range(N - 2, -1, -1):
            if r[i] > r[i + 1] and cy[i] <= cy[i + 1]:
                cy[i] = cy[i + 1] + 1
        
        return sum(cy)