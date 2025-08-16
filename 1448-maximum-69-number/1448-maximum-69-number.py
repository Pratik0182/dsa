class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for idx, val in enumerate(num):
          if val == '6':
            num[idx] = '9'
            break
        return int("".join(num))