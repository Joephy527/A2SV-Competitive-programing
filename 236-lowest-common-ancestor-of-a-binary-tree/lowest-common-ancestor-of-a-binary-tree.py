# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return node, False, False

            left, is_node_left, is_parent_left = dfs(node.left)
            right, is_node_right, is_parent_right = dfs(node.right)

            if is_parent_left or is_parent_right:
                val = left if is_parent_left else right
                return val, False, True

            val = node
            is_cur = node in (p, q)
            is_node = is_node_left or is_node_right or is_cur
            
            if (
                (is_node_left and is_node_right) or
                (is_node_left or is_node_right) and is_cur
            ):
                return val, is_node, True

            if is_node_left:
                val = left
            elif is_node_right:
                val = right

            return val, is_node, False

        return dfs(root)[0]