class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set("+-*/")
        for v in tokens:
          if v not in op:
            stack.append(int(v))
          else:
            v2, v1 = stack.pop(), stack.pop()
            if v == "+":
              stack.append(v1 + v2)
            elif v == "-":
              stack.append(v1 - v2)
            elif v == "*":
              stack.append(v1 * v2)
            else:
              stack.append(int(v1 / v2))
        return stack[0]
