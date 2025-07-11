class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent, weight = {}, {}
        answer = [-1.0] * len(queries)

        def find(u):
            if u not in parent:
                parent[u] = u
                weight[u] = 1.0
            elif parent[u] != u:
                cur_parent = parent[u]
                parent[u] = find(cur_parent)
                weight[u] *= weight[cur_parent]

            return parent[u]

        def union(u, v, w):
            parent_u, parent_v = find(u), find(v)
            
            if parent_u != parent_v:
                parent[parent_u] = parent_v
                weight[parent_u] = weight[v] * w / weight[u]

        for (u, v), w in zip(equations, values):
            union(u, v, w)

        for i, (u, v) in enumerate(queries):
            if u in parent and v in parent:
                parent_u, parent_v = find(u), find(v)
                
                if parent_u == parent_v:
                    answer[i] = weight[u] / weight[v]

        return answer