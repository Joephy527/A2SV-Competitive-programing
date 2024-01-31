# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            nonlocal ans
            
            if not node: return

            if node.val >= m:
                ans += 1

            m = max(m, node.val)
            dfs(node.left, m)
            dfs(node.right, m)

        ans = 0
        dfs(root, root.val)

        return ans
