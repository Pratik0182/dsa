class Solution:
    def canBeTypedWords(self, text: str, bl: str) -> int:
        broken = set(bl)
        data = text.split(" ")
        res = len(data)
        for word in data:
          for ch in word:
            if ch in broken:
              res -= 1
              break
        return res