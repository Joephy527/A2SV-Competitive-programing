# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return [0, float("-inf")]

            left = dfs(node.left)
            right = dfs(node.right)

            if left[0] >= right[0]:
                maxH = left[0] + 1
                leftMost = left[1] if left[1] != float("-inf") else node.val
            else:
                maxH = right[0] + 1
                leftMost = right[1] if right[1] != float("-inf") else node.val

            return [maxH, leftMost]

        return dfs(root)[1]
