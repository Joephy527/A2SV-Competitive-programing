# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return

        maxIdx = 0
        for i in range(len(nums)):
            if nums[i] > nums[maxIdx]:
                maxIdx = i

        root = TreeNode(nums[maxIdx])
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx + 1:])

        return root
