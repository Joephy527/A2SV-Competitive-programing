class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestorList = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)

        def dfs(vertex, ancestor):
            for dest in graph[vertex]:
                if not ancestorList[dest] or ancestorList[dest][-1] != ancestor:
                    ancestorList[dest].append(ancestor)
                    dfs(dest, ancestor)

        for i in range(n):
            dfs(i, i)

        return ancestorList
