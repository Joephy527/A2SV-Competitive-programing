# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        ans = self.isSame(root, subRoot)

        l, r = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)
        
        return l or r or ans

    def isSame(self, p, q):
        if not p and not q:
            return True
        elif (not p and q) or (p and not q) or (p.val != q.val):
            return False
        else:
            l, r = self.isSame(p.left, q.left), self.isSame(p.right, q.right)
            
            return l and r
