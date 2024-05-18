# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if node==None: return 0
            
            moves=dfs(node.left, node) + dfs(node.right, node)
            x = node.val - 1
            
            if parent: parent.val += x
            
            moves += abs(x)
            
            return moves
        
        return dfs(root, None)
