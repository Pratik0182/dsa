# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        def helper(left, right, level):
            if not left:
                return
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
            helper(left.left, right.right, level + 1)
            helper(left.right, right.left, level + 1)
        helper(root.left, root.right, 1)
        return root