class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0] * n
        vertices = []

        for u, v in edges:
            inDegree[v] = 1

        for vertice in range(n):
            if not inDegree[vertice]:
                vertices.append(vertice)

        return vertices
