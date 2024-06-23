class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        maxDetonations = 0
        
        for i in range(n):
            for j in range(n):
                if i != j and self.isInRange(bombs[i], bombs[j]):
                    graph[i].append(j)

        for i in range(n):
            visited = set()
            maxDetonations = max(maxDetonations, self.dfs(i, visited, graph))
        
        return maxDetonations

    def isInRange(self, bombOne, bombTwo):
        x1, y1, r = bombOne
        x2, y2, _ = bombTwo
        
        return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r ** 2

    def dfs(self, node, visited, graph):
        if node in visited:
            return 0
        
        visited.add(node)
        detonantions = 1
        
        for neigh in graph[node]:
            detonantions += self.dfs(neigh, visited, graph)
        
        return detonantions
