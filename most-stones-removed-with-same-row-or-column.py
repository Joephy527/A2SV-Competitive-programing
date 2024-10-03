class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = defaultdict(list)
        visited = set()
        connected = 0

        def dfs(stone):
            visited.add(stone)

            for neigh in graph[stone]:
                if neigh not in visited:
                    dfs(neigh)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1

        return n - connected
