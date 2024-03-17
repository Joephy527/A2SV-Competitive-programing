# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        targetNode = None
        
        def dfs(ogNode, clonedNode):
            nonlocal targetNode
            
            if not ogNode: return

            if ogNode == target:
                targetNode = clonedNode
                return

            dfs(ogNode.left, clonedNode.left)
            dfs(ogNode.right, clonedNode.right)

        dfs(original, cloned)

        return targetNode
