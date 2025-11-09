class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
      n = len(wall)
      if wall[0] == 1:
        return n
      table = defaultdict(int)
      for r in wall:
        val = 0
        for b in r[:-1]:
          val += b
          table[val] += 1
      sub = max(table.values()) if table else 0
      print(table)
      return n - sub