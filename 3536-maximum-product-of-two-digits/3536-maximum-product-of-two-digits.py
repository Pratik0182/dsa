class Solution:
    def maxProduct(self, n: int) -> int:
        arr = list(map(lambda i: -int(i), list(str(n))))
        heapify(arr)
        n1, n2 = -heappop(arr), -heappop(arr)
        return n1 * n2