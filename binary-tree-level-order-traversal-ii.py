# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return

        bottomUpOrder = deque()
        queue = deque([root])

        while queue:
            levelVal = []
            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                levelVal.append(node.val)
                
                if node.left: queue.append(node.left)
                
                if node.right: queue.append(node.right)

            bottomUpOrder.appendleft(levelVal)

        return bottomUpOrder
