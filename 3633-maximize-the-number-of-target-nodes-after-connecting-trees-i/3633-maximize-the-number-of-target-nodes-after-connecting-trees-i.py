class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for ai, bi in edges1:
            graph1[ai].append(bi)
            graph1[bi].append(ai)
        for ui, vi in edges2:
            graph2[ui].append(vi)
            graph2[vi].append(ui)
        def dfs(node, graph, level, seen):
            seen.add(node)
            if level == 0:
                return 1
            ret = [0]
            for nei in graph[node]:
                if nei not in seen:
                    ret.append(dfs(nei, graph, level - 1, seen))
            return 1 + sum(ret)
        res = []
        mx = None
        if k <= 1:
            mx = k
        else:
            for i in range(len(edges2) + 1):
                mx = max(mx, dfs(i, graph2, k - 1, set()))
        for i in range(len(edges1) + 1):
            res.append(dfs(i, graph1, k, set()) + mx)
        return res