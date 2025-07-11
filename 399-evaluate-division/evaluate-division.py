class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        answer = [-1.0] * len(queries)

        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1 / val
            graph[u][u] = graph[v][v] = 1.0

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    if i == j:
                        continue
                    
                    graph[i][j] = graph[i][k] * graph[k][j]

        for i, (u, v) in enumerate(queries):
            answer[i] = graph[u].get(v, -1.0)

        return answer