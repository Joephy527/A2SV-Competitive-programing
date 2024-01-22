# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left

            suc = self.inorderSuc(root.right)
            root.val = suc.val
            root.right = self.deleteNode(root.right, suc.val)

        return root

    def inorderSuc(self, node):
        while node.left:
            node = node.left

        return node
