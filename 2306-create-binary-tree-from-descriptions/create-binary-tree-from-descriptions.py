# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = {}

        for parent, child, is_left in descriptions:
            if parent not in parents:
                parents[parent] = TreeNode(parent)

            if child not in parents:
                parents[child] = TreeNode(child)

            child_node = parents[child]
            parent_node = parents[parent]
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            children.add(child)

        for parent in parents:
            if parent not in children:
                return parents[parent]