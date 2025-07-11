class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        answer = [-1.0] * len(queries)

        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0

            if src == dest:
                return 1.0

            visited.add(src)

            for neigh, val in graph[src]:
                if neigh not in visited:
                    cur = dfs(neigh, dest, visited)

                    if cur != -1.0:
                        return cur * val

            return -1.0

        for i, (u, v) in enumerate(queries):
            answer[i] = dfs(u, v, set())

        return answer