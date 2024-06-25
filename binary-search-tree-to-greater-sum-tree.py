# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        runningSum = 0
        
        def reverseInorder(node):
            if not node: return

            nonlocal runningSum

            reverseInorder(node.right)

            runningSum += node.val
            node.val = runningSum
            
            reverseInorder(node.left)

        reverseInorder(root)

        return root
