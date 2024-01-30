# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            r = None
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                
                if node:
                    r = node
                    queue.append(node.left)
                    queue.append(node.right)

            if r: res.append(r.val)

        return res
