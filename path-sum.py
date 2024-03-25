# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return

        def dfs(node, prevSum):
            if not node: return

            curSum = node.val + prevSum

            if curSum == targetSum and not node.left and not node.right:
                return True

            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum))

        return dfs(root, 0)
