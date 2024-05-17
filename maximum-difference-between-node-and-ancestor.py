# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def dfs(node, low, high):
            if not node:
                return

            ans[0] = max(ans[0], abs(node.val - low), abs(node.val - high))
            low = min(low, node.val)
            high = max(high, node.val)

            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, root.val, root.val)

        return ans[0]
