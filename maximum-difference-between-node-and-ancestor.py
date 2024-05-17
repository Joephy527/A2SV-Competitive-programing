# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right:
                return (node.val, node.val, 0)

            left = dfs(node.left) if node.left else (node.val, node.val, 0)
            right = dfs(node.right) if node.right else (node.val, node.val, 0)

            low = min(node.val, left[0], right[0])
            high = max(node.val, left[1], right[1])
            maxDiff = (max(abs(node.val - left[0]), abs(node.val - right[0]),
                       abs(node.val - left[1]), abs(node.val - right[1]),
                       left[2], right[2]))

            return (low, high, maxDiff)

        return dfs(root)[2]
