class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for ai, bi in edges1:
            graph1[ai].append(bi)
            graph1[bi].append(ai)
        for ai, bi in edges2:
            graph2[ai].append(bi)
            graph2[bi].append(ai)
        n, m = len(edges1) + 1, len(edges2) + 1
        def dfs(graph, node, parent, colour, is1):
            nonlocal even1, even2, odd1, odd2
            if colour[node] == 0:
                if is1:
                    even1 += 1
                else:
                    even2 += 1
            else:
                if is1:
                    odd1 += 1
                else:
                    odd2 += 1
            for nei in graph[node]:
                if nei != parent:
                    colour[nei] = 1 - colour[node]
                    dfs(graph, nei, node, colour, is1)
        even1 = even2 = odd1 = odd2 = 0
        colour1 = [-1] * n
        colour1[0] = 0
        colour2 = [-1] * m
        colour2[0] = 0
        dfs(graph1, 0, -1, colour1, True)
        dfs(graph2, 0, -1, colour2, False)
        mmax = max(even2, odd2)
        res = [0] * n
        for i in range(n):
            res[i] = (even1 if colour1[i] == 0 else odd1) + mmax
        return res