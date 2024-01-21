# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        
        if not node:
            return TreeNode(val)

        if node.val < val:
            node.right = self.insertIntoBST(node.right, val)
        else:
            node.left = self.insertIntoBST(node.left, val)

        return root
