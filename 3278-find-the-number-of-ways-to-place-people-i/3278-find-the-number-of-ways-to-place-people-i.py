class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        points = sorted(points, key = lambda x: (-x[1], x[0]))
        for i in range(len(points)):
          x0, y0 = points[i][0], points[i][1]
          xc = float('inf')
          for j in range(i + 1, len(points)):
            xi, yi = points[j][0], points[j][1]
            if xi >= x0 and xi < xc:
              xc = xi
              res += 1
        return res