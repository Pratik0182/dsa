class Solution:
    def kthCharacter(self, k: int) -> str:
        data = list('abcdefghijklmnopqrstuvwxyz')
        arr = {val : idx + 1 for idx, val in enumerate(data)}
        res = ['a']
        while len(res) <= k:
            curr = []
            for c in res:
                curr.append(data[arr[c] % 26])
            res += curr
        return res[k - 1]