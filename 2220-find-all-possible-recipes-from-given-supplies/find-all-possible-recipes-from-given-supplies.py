class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_idx = {r: i for i, r in enumerate(recipes)}
        can_make = {supply: True for supply in supplies}

        def dfs(vertex, visited):
            if can_make.get(vertex, False):
                return True

            if vertex not in recipes_idx or vertex in visited:
                return False

            visited.add(vertex)
            
            can_make[vertex] = all(
                dfs(r, visited) for r in ingredients[recipes_idx[vertex]]
            )

            return can_make[vertex]

        return [r for r in recipes if dfs(r, set())]