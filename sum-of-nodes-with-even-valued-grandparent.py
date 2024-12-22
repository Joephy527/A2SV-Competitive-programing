# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        evenSum = [0]
        
        def dfs(node, parent, grandParent):
            if not node: return

            if not grandParent % 2:
                evenSum[0] += node.val

            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)

        dfs(root, 1, 1)

        return evenSum[0]
