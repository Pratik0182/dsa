from collections import deque
class Solution(object):
  def totalFruit(self, fruits):
    data = deque()
    freq = {}
    res = curr = 0
    for idx, val in enumerate(fruits):
      if val not in freq and len(freq) == 2:
        data.append(val)
        freq[val] = 1
        res = max(res, curr)
        curr += 1
        while len(freq) == 3:
          val = data.popleft()
          curr -= 1
          freq[val] -= 1
          if freq[val] == 0:
            del freq[val]
      else:
        if val in freq:
          freq[val] += 1
        else:
          freq[val] = 1
        curr += 1
        data.append(val)
    return max(res, curr)
        