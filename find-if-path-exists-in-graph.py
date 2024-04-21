class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                        return True

        return dfs(source)
