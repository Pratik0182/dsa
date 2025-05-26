class NumArray(object):

    def __init__(self, nums):
        self.N = len(nums)
        self.tree = [0] * (self.N + 1)
        self.nums = nums
        for k in range(1, self.N + 1):
            p = k & -k
            self.tree[k] = sum(nums[k - p : k])

    def update(self, index, val):
        new = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.N:
            self.tree[index] += new
            index += index & -index

    def sumRange(self, left, right):
        res = 0
        right += 1
        while right >= 1:
            res += self.tree[right]
            right -= right & -right
        while left >= 1:
            res -= self.tree[left]
            left -= left & -left
        return res



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)