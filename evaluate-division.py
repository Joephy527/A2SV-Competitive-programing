class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for equation, val in zip(equations, values):
            u, v = equation

            graph[u][v] = val
            graph[v][u] = 1 / val

        def dfs(numerator, denominator):
            if numerator not in graph or denominator not in graph:
                return -1.0
            
            if numerator == denominator:
                return 1.0
            
            visited.add(numerator)
            
            for v in graph[numerator]:
                if v not in visited:
                    ans = dfs(v, denominator)
                    
                    if ans != -1:
                        return graph[numerator][v] * ans

            return -1

        answer = []
        
        for numerator, denominator in queries:
            visited = set()
            
            answer.append(dfs(numerator, denominator))

        return answer
