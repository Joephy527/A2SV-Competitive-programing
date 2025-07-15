class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()

        for a, b in prerequisites:
            indegree[b] += 1
            graph[a].append(b)

        for v in range(len(indegree)):
            if not indegree[v]:
                queue.append(v)

        while queue:
            v = queue.popleft()
            
            for neigh in graph[v]:
                indegree[neigh] -= 1

                if not indegree[neigh]:
                    queue.append(neigh)

        return not sum(indegree)