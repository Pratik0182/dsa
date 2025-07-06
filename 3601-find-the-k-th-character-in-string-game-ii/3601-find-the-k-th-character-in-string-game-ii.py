class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        data = list('abcdefghijklmnopqrstuvwxyz')
        i = 0
        while k != 1:
            curr = int(log2(k - 1))
            if operations[curr] == 1:
                i += 1
            k -= 1 << curr
        return data[i % 26]