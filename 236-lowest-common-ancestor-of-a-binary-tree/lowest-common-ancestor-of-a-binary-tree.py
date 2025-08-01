# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if (
                left and right or
                node.val in (p.val, q.val)
            ):
                return node

            return left if left else right

        return dfs(root)