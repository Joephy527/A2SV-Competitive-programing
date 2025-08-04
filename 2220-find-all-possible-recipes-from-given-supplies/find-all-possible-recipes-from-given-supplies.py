class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = defaultdict(list)
        visited = set()

        for rec, ing in zip(recipes, ingredients):
            graph[rec] = ing

        def dfs(rec):
            if rec in supplies:
                return True

            if rec not in graph:
                return False

            visited.add(rec)

            for ing in graph[rec]:
                if ing in visited or not dfs(ing):
                    return False

            visited.remove(rec)
            supplies.add(rec)

            return True

        return [rec for rec in recipes if dfs(rec)]