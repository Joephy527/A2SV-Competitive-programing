# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if not node: return ""

            if node.val == target: return path

            path.append("L")
            left = dfs(node.left, path, target)
            
            if left: return left
            
            path.pop()
            path.append("R")
            right = dfs(node.right, path, target)
            
            if right: return right

            path.pop()

            return ""

        start = dfs(root, [], startValue)
        finish = dfs(root, [], destValue)

        i = 0

        while i < len(min(start, finish)) and start[i] == finish[i]:
            i += 1

        shortestPath = ["U"] * (len(start) - i) + finish[i:]

        return "".join(shortestPath)
