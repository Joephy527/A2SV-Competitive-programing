# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def getCurVal(i):
            val = 0

            while i < len(traversal) and traversal[i] != "-":
                val = (val * 10) + int(traversal[i])
                i += 1

            return (val, i)

        rootVal, idx = getCurVal(0)

        levelMap = defaultdict(list)
        levelMap[0].append(TreeNode(rootVal))
        curLevel = 0

        while idx < len(traversal):
            if traversal[idx] == "-":
                curLevel += 1
            else:
                val, idx = getCurVal(idx)
                
                parent = levelMap[curLevel - 1][-1]
                child = TreeNode(val)

                if not parent.left:
                    parent.left = child
                else:
                    parent.right = child
                
                levelMap[curLevel].append(child)
                curLevel = 1

            idx += 1

        return levelMap[0][0]
