class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = [[] for _ in range(n)]
        queue = deque()
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        for v in range(n):
            if indegree[v] == 1:
                queue.append(v)

        while n > 2:
            leaveCount = len(queue)
            
            for _ in range(leaveCount):
                leaf = queue.popleft()

                for neigh in graph[leaf]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        queue.append(neigh)

            n -= leaveCount

        return list(queue)
