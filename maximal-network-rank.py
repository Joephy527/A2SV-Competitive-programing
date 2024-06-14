class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        maxNetworkRank = 0

        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        for i in range(n):
            for j in range(i + 1, n):
                curNetworkRank = len(graph[i]) + len(graph[j]) - (j in graph[i]) 
                maxNetworkRank = max(maxNetworkRank, curNetworkRank)

        return maxNetworkRank
