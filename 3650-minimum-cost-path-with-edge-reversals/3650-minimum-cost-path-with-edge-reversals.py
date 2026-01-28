class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y, w in edges:
          graph[x].append((y, w))
          graph[y].append((x, 2 * w))
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
          d, x = heappop(heap)
          if x == n - 1:
            return d
          if d != dist[x]:
            continue
          for y, w in graph[x]:
            if dist[x] + w < dist[y]:
              dist[y] = dist[x] + w
              heappush(heap, (dist[y], y))
        return -1