# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            length = len(queue)
            cur = []

            for _ in range(length):
                node = queue.popleft()

                if node:
                    cur.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    cur.append(float("inf"))

            if cur != cur[::-1]:
                return False

        return True
