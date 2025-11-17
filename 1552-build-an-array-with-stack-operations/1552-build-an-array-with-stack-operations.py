class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
      curr = 0
      res = []
      for v in target:
        count = 0
        curr += 1 
        while curr != v:
          count += 1
          curr += 1
        res.extend(["Push", "Pop"] * count)
        res.append("Push")
      return res