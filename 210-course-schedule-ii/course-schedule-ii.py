class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        path = []

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)

        for v in range(len(indegree)):
            if not indegree[v]:
                queue.append(v)

        while queue:
            v = queue.popleft()
            path.append(v)
            
            for neigh in graph[v]:
                indegree[neigh] -= 1

                if not indegree[neigh]:
                    queue.append(neigh)

        return path if not sum(indegree) else []