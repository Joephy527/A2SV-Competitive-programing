class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorMap = {}
        
        def dfs(vertex, color):
            if vertex in colorMap:
                if colorMap[vertex] != color:
                    return
                else:
                    return True
            
            colorMap[vertex] = color

            for u in graph[vertex]:
                if not dfs(u, -1 * color):
                    return

            return True

        for i in range(len(graph)):
            if i not in colorMap and not dfs(i, -1):
                return

        return True
