# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, m):
            nonlocal ans
            
            if not node: return

            newM = m

            if node.val >= m:
                ans += 1
                newM = node.val

            dfs(node.left, newM)
            dfs(node.right, newM)

        dfs(root, root.val)

        return ans
