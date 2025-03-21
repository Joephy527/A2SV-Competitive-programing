class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        visited = {supply: 1 for supply in supplies}
        recipes_created = []

        for idx, r in enumerate(recipes):
            graph[r] = ingredients[idx]

        def dfs(vertex):
            if not graph[vertex]:
                return vertex in supplies
            
            visited[vertex] = -1
            
            for r in graph[vertex]:
                if r not in visited:
                    visited[r] = dfs(r)

                if visited[r] == 0 or visited[r] == -1:
                    return 0

            return 1

        for r in recipes:
            if r not in visited:
                visited[r] = dfs(r)

            if visited[r] == 1:
                recipes_created.append(r)

        return recipes_created