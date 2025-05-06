# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        res = [0]
        def dfs(node, cmin, cmax):
            if not node:
                return 
            cmin = min(cmin, node.val)
            cmax = max(cmax, node.val)
            res[0] = max(res[0], cmax - cmin)
            dfs(node.left, cmin, cmax)
            dfs(node.right, cmin, cmax)
            return res[0]
        return dfs(root, 10001, -1)