# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, curStr):
            curStr = chr(node.val + ord("a")) + curStr
            
            if not node.left and not node.right:
                return curStr

            if not node.right:
                return dfs(node.left, curStr)
            elif not node.left: 
                return dfs(node.right, curStr)
            
            return min(dfs(node.left, curStr), dfs(node.right, curStr))

        return dfs(root, "")
