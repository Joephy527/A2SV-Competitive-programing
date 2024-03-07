# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        rootToLeaf = []
        subPath = [root]

        def backTrack(node):
            if not node.left and not node.right:
                rootToLeaf.append("->".join([str(node.val) for node in subPath]))

                return

            if node.left:
                subPath.append(node.left)
                backTrack(node.left)
                subPath.pop()

            if node.right:
                subPath.append(node.right)
                backTrack(node.right)
                subPath.pop()

        backTrack(root)

        return rootToLeaf
