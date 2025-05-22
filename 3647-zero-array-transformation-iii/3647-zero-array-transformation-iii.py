class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.tree = [0] * (4 * self.N)
        self.lp = [0] * (4 * self.N)
        self.build(1, 0, self.N - 1, arr)
    
    def build(self, k, l, r, arr):
        if l == r:
            self.tree[k] = arr[l]
            return arr[l]
        else:
            mid = (l + r) // 2
            self.tree[k] = max(self.build(2 * k, l, mid, arr), self.build(2 * k + 1, mid + 1, r, arr))
            return self.tree[k]
    
    def update(self, L, R, v, k, l, r):
        if L > r or R < l:
            return 
        if L <= l and R >= r:
            self.tree[k] += v
            self.lp[k] += v
            return
        if self.lp[k]:
            for n in (2 * k, 2 * k + 1):
                self.tree[n] += self.lp[k]
                self.lp[n] += self.lp[k]
            self.lp[k] = 0
        mid = (l + r) // 2
        self.update(L, R, v, 2 * k, l, mid)
        self.update(L, R, v, 2 * k + 1, mid + 1, r)
        self.tree[k] = max(self.tree[2 * k], self.tree[2 * k + 1])

    def mmax(self, L, R, k, l, r):
        if L > r or R < l:
            return -float('inf')
        if L <= l and R >= r:
            return self.tree[k]
        if self.lp[k]:
            for n in (2 * k, 2 * k + 1):
                self.tree[n] += self.lp[k]
                self.lp[n] += self.lp[k]
            self.lp[k] = 0
        mid = (l + r) // 2
        left = self.mmax(L, R, 2 * k, l, mid)
        right = self.mmax(L, R, 2 * k + 1, mid + 1, r)
        return max(left, right)
    
class Solution(object):
    def maxRemoval(self, nums, queries):
        N = len(nums)
        M = len(queries)
        memo = defaultdict(int)
        curr = 0
        for l, r in queries:
            memo[l] += 1
            memo[r + 1] -= 1
        for idx, val in enumerate(nums):
            curr += memo.get(idx, 0)
            if curr < val:
                return -1
        st = SegmentTree(nums)
        queries.sort(key = lambda x: (x[0], x[1]))
        res = 0
        curr = []
        qidx = -1
        i = 0
        while i < N:
            while qidx + 1 < M and queries[qidx + 1][0] == i:
                qidx += 1
                heappush(curr, -queries[qidx][1])
            while st.mmax(i, i, 1, 0, N - 1) > 0:
                if not curr or -curr[0] < i:
                    return -1
                C = -heappop(curr)
                st.update(i, C, -1, 1, 0, N - 1)
                res += 1
            i += 1
        return M - res
        