# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = float("-inf")

        def dfs(node):
            nonlocal maxPathSum

            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            curMaxPathSum = max(left, right) + node.val
            subTreeSum = curMaxPathSum + min(left, right)

            maxPathSum = max(maxPathSum, curMaxPathSum, subTreeSum, node.val)

            return max(curMaxPathSum, node.val)

        dfs(root)

        return maxPathSum
