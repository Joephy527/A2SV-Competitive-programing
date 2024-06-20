class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = {}

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(v):
            if v in visited:
                if visited[v]:
                    return
                else:
                    return True
            
            visited[v] = 1

            for u in graph[v]:
                if not dfs(u): return

            visited[v] = 0

            return True

        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return

        return True
