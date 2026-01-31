class Solution:
    def reverseByType(self, s: str) -> str:
      ch, sp = deque([]), deque([])
      for c in s:
        if c.isalpha():
          ch.append(c)
        else:
          sp.append(c)
      res = []
      for c in s:
        if c.isalpha():
          res.append(ch.pop())
        else:
          res.append(sp.pop())
      return "".join(res)