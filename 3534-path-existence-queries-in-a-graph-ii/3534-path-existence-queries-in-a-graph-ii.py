class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        '''
        0 1 2 3 4
        2
        0 -> 1, 2
        1 -> 0, 2, 3 
        2 -> 0, 1, 3 4
        3 -> 1, 2, 4        
        4 -> 2, 3
        '''
        sorted_nodes = sorted(enumerate(nums), key = lambda x:x[1])

        get_idx = [0] * len(nums)
        for i,(node,val) in enumerate(sorted_nodes):
            get_idx[node] = i
        LOG = (10 ** 5).bit_length()
        dp = [[0] * LOG for _ in range(len(nums))]

        right = 0
        for i in range(len(sorted_nodes)):
            while right < len(nums) and abs(sorted_nodes[i][-1] - sorted_nodes[right][-1]) <= maxDiff:
                right += 1
            dp[i][0] = right - 1
        for i in range(1,LOG):
            for j in range(len(nums)):
                dp[j][i] = dp[dp[j][i-1]][i-1]
        res = []
        for u,v in queries:
            a = get_idx[u]
            b = get_idx[v]
            if a == b:
                res.append(0)
                continue
            if a < b:
                a,b = b,a
            count = 0
            for i in range(LOG-1,-1,-1):
                if dp[b][i] < a:
                    b = dp[b][i]
                    count += (1<<i)
            if dp[b][0] >= a:
                res.append(count+1)
            else:
                res.append(-1)
        return res