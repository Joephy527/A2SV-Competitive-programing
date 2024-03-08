# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root,1,0]])
        maxLevelWidth = 0
        prevLevel, prevNum = 0, 1

        while queue:
            node, num, level = queue.popleft()

            if level > prevLevel:
                prevLevel = level
                prevNum = num
            
            maxLevelWidth = max(maxLevelWidth, num - prevNum + 1)

            if node.left:
                queue.append([node.left, 2 * num, level + 1])
            if node.right:
                queue.append([node.right, 2 * num + 1, level + 1])

        return maxLevelWidth
