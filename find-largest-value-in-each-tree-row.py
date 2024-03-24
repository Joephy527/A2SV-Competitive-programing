# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return

        queue= deque([root])
        biggest = []

        while queue:
            length = len(queue)
            maxNum = float("-inf")

            for _ in range(length):
                node = queue.popleft()
                maxNum = max(maxNum, node.val)

                if node.left: queue.append(node.left)
                
                if node.right: queue.append(node.right)

            biggest.append(maxNum)

        return biggest
