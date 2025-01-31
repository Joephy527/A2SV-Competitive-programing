class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n))
        rank = [1] * n

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])

            return parent[v]

        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2: return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for i, (u, v) in enumerate(edges):
            if not union(u - 1, v - 1):
                return edges[i]
