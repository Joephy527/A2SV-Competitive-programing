# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        swaps = 0

        def getLevelSwaps(nums, idxMap, sortedNums):
            levelSwaps = 0

            for i, val in enumerate(sortedNums):
                ogIdx = idxMap[val]
                
                if ogIdx != i:
                    levelSwaps += 1
                    nums[i], nums[ogIdx] = nums[ogIdx], nums[i]
                    idxMap[val] = i
                    idxMap[nums[ogIdx]] = ogIdx

            return levelSwaps

        while queue:
            idxMap = {}
            level = []

            for idx in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                idxMap[node.val] = idx

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            swaps += getLevelSwaps(level, idxMap, sorted(level))

        return swaps
