class Solution(object):
    def maxScore(self, n, edges):
         #is0 -- no neighbours, is1 --- cycle hain
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        seen = [False] * n
        comps = []
        ##DFs
        for i in range(n):
            if not seen[i]:
                stack = [i]
                comp = []
                seen[i] = True
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    for neighbor in adj[node]:
                        if not seen[neighbor]:
                            seen[neighbor] = True
                            stack.append(neighbor)
                m = sum(degree[x] for x in comp) // 2
                k = len(comp)
        #is0 -- no neighbours, is1 --- cycle hain
                is0 = (m == 0)
                is1 = (m == k)
                comps.append((is0, is1, comp))
        def sort_key(t):
            is0, is1, comp = t
            if is0:
                return (2, 0)
            if is1:
                return (0, -len(comp))
            return (1, -len(comp))
        comps.sort(key=sort_key)
        print(comps)
        labels = list(range(n, 0, -1))
        ptr = 0
        values = [0] * n
        for is0, is1, comp in comps:
            k = len(comp)
            h = labels[ptr:ptr+k]
            ptr += k
            if is0:
                values[comp[0]] = h[0]
            elif not is1:
                s = next(z for z in comp if degree[z] == 1)
                path = []
                prev, curr = -1, s
                while True:
                    path.append(curr)
                    nexts = [nei for nei in adj[curr] if nei != prev]
                    if not nexts:
                        break
                    prev, curr = curr, nexts[0]
                evens = h[1::2][::-1]
                odds = h[::2]
                assigned = evens + odds
                for i, node in enumerate(path):
                    values[node] = assigned[i]
            else:
                path = comp
                odds = h[::2]
                evens = h[1::2][::-1]
                #even odd maximize propertyY
                assigned = odds + evens
                for i, node in enumerate(path):
                    values[node] = assigned[i]
        return sum(values[u] * values[v] for u, v in edges)