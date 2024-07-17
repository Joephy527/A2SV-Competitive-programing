"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}

        def dfs(vertex):
            if vertex in graph:
                return graph[vertex]
            
            newVertex = Node(vertex.val)
            graph[vertex] = newVertex

            for child in vertex.neighbors:
                newVertex.neighbors.append(dfs(child))
                
            return newVertex

        return dfs(node) if node else None
