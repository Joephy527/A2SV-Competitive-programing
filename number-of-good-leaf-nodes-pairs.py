# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs = [0]

        def dfs(node):
            if not node: return []

            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        pairs[0] += 1

            distList = left + right

            return [d + 1 for d in distList]

        dfs(root)

        return pairs[0]
