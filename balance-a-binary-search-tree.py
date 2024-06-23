# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodeArr = []
        
        self.orderedTreeList(nodeArr, root)

        return self.balance(nodeArr, 0, len(nodeArr) - 1)
    
    def orderedTreeList(self, nodeArr, node):
        if not node: return

        self.orderedTreeList(nodeArr, node.left)
        nodeArr.append(node)
        self.orderedTreeList(nodeArr, node.right)

    def balance(self, nodeArr, left, right):
        if left > right: return

        mid = (left + right) // 2
        nodeArr[mid].left = self.balance(nodeArr, left, mid - 1)
        nodeArr[mid].right = self.balance(nodeArr, mid + 1, right)

        return nodeArr[mid]
