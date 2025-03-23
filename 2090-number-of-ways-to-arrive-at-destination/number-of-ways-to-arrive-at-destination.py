class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        mod = (10 ** 9) + 7
        heap = [(0, 0)]
        shortest_time = [float("inf")] * n
        path_count = [0] * n

        shortest_time[0] = 0
        path_count[0] = 1

        for a, b, t in roads:
            graph[a].append((b, t))
            graph[b].append((a, t))

        while heap:
            time, vertex = heappop(heap)

            if time > shortest_time[vertex]:
                continue

            for neigh, t in graph[vertex]:
                if time + t < shortest_time[neigh]:
                    shortest_time[neigh] = time + t
                    path_count[neigh] = path_count[vertex]
                    heappush(
                        heap, (shortest_time[neigh], neigh)
                    )
                elif time + t == shortest_time[neigh]:
                    path_count[neigh] = (
                        path_count[neigh] + path_count[vertex]
                    ) % mod

        return path_count[n - 1]