# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandParent):
            if not node:
                return 0

            left = dfs(node.left, node.val, parent)
            right = dfs(node.right, node.val, parent)

            return left + right + (node.val if not grandParent % 2 else 0)

        return dfs(root, 1, 1)
