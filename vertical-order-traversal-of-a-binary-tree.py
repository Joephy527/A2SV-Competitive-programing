# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([[root, 0]])
        colGroup = defaultdict(list)

        while queue:
            rowGroup = defaultdict(list)

            for _ in range(len(queue)):
                node, col = queue.popleft()

                rowGroup[col].append(node.val)

                if node.left: queue.append([node.left, col - 1])
                if node.right: queue.append([node.right, col + 1])

            for col in rowGroup:
                colGroup[col].extend(sorted(rowGroup[col]))

        sortedDict = dict(sorted(colGroup.items()))

        return sortedDict.values()
