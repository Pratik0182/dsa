class Solution:
    def sortVowels(self, s: str) -> str:
        order = list('AEIOUaeiou')
        data = []
        for ch in s:
          if ch in order:
            data.append(ch)
        
        data = deque(sorted(data, key = lambda x: order.index(x)))
        s = list(s)
        for idx, ch in enumerate(s):
          if ch in order:
            s[idx] = data.popleft()
        return "".join(s)