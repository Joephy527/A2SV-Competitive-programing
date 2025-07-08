# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        level = []

        while queue:
            cur = []
            
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

                    cur.append(node.val)

            if cur:
                level.append(cur)

        return level