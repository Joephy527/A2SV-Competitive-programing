# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_leftmost(node, parent):
            while node.left:
                parent = node
                node = node.left

            if parent.left == node:
                parent.left = node.right

            return node
        
        def dfs(node):
            if not node:
                return

            if node.val == key:
                if not node.left:
                    return node.right

                if not node.right:
                    return node.left
                
                l = get_leftmost(node.right, node)
                l.left = node.left
                l.right = node.right if l != node.right else l.right

                return l

            if node.val < key:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)

            return node

        return dfs(root)