from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = deque(digits)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
          if not carry:
            break
          elif carry and q[i] == 9:
            q[i] = 0
          elif q[i] != 9:
            q[i] += 1
            carry = 0
        if carry:
          q.appendleft(1)
        return list(q)