class Solution(object):
    def largestPathValue(self, colors, edges):
        N = len(colors)
        graph = defaultdict(list)
        indegree = [0] * N
        path = [defaultdict(int) for _ in range(N)]
        seen = 0
        res = 1
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        q = deque([i for i in range(N) if indegree[i] == 0])
        while q:
            curr = q.popleft()
            seen += 1
            curr_col = colors[curr]
            path[curr][curr_col] += 1
            res = max(res, path[curr][curr_col])
            for nei in graph.get(curr, []):
                for c in path[curr]:
                    path[nei][c] = max(path[nei][c], path[curr][c])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if seen == N else -1