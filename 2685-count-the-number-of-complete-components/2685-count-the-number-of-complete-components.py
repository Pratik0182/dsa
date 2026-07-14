class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        read = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        for u in range(n):
            if u in read: #already analyzed
                continue
            read.add(u)
            com = [u]
            q = deque([u])
            while q:
                node = q.popleft()
                for v in graph[node]:
                    if v not in read:
                        read.add(v)
                        com.append(v)
                        q.append(v)
            edg = len(com) #to check the same no. of edges for other
            flag = 0

            #connected component (all edges having degree == edg - 1)
            for v in com:
                if len(graph[v]) != edg - 1:
                    flag = 1
                    break
            res += 1 if not flag else 0
        return res
