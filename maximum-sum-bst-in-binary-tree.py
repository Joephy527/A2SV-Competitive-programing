# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum = 0

        def dfs(node):
            nonlocal maxSum

            if not node:
                return ["Empty", 0, None, None]

            leftStatus, leftSum, leftLowest, leftHighest = dfs(node.left)
            rightStatus, rightSum, rightLowest, rightHighest = dfs(node.right)

            if (((leftStatus == "BST" and leftHighest < node.val) or
                leftStatus == "Empty") and
                ((rightStatus == "BST" and rightLowest > node.val) or
                rightStatus == "Empty")):
                
                curSum = leftSum + node.val + rightSum
                maxSum = max(maxSum, curSum)

                return [
                    "BST",
                    curSum,
                    leftLowest if leftLowest else node.val,
                    rightHighest if rightHighest else node.val,
                    ]

            return ["", None, None, None]

        dfs(root)

        return maxSum
