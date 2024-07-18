# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = set([root])
        toDelete = set(to_delete)

        def dfs(node):
            if not node:
                return

            if node.val in toDelete:
                forest.discard(node)

                if node.left: forest.add(node.left)
                if node.right: forest.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            return node if node.val not in toDelete else None

        dfs(root)

        return list(forest)
