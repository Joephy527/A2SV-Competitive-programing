# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if node is None:
                return
            
            if d == 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)

                return

            dfs(node.left, d - 1)
            dfs(node.right, d - 1)

        if depth == 1:
            return TreeNode(val, root)

        dfs(root, depth - 1)
        
        return root
