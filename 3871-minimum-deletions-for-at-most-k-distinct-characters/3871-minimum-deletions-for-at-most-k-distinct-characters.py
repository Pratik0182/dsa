class Solution(object):
    def minDeletion(self, s, k):
        D = Counter(s)
        if set(s) <= k:
            return 0
        else:
            data = [[D[v], v] for v in set(s)]
            heapify(data)
            res = 0
            for i in range(len(set(s)) - k):
                rem, _ = heappop(data)
                res += rem
            return res