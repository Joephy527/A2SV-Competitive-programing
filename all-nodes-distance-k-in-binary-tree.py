# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        
        graph = defaultdict(list)
        
        def buildGraph(node, parent=None):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                
                if node.left:
                    buildGraph(node.left, node)
                
                if node.right:
                    buildGraph(node.right, node)
        
        buildGraph(root)
        
        queue = deque([(target.val, 0)])  # (node value, current distance)
        visited = set([target.val])
        values = []
        
        while queue:
            curNode, curDistance = queue.popleft()
            
            if curDistance == k:
                values.append(curNode)
            
            for neigh in graph[curNode]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, curDistance + 1))
        
        return values
