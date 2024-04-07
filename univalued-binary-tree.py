# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val

        def dfs(node):
            nonlocal val

            if not node:
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            return left and right and node.val == val

        return dfs(root)
