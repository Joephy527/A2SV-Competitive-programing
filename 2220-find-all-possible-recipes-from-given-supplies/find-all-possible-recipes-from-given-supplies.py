class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}
        queue = deque(supplies)
        cookable = []

        for rec, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                graph[ing].append(rec)

            indegree[rec] = len(ingredient)

        while queue:
            ing = queue.popleft()

            for rec in graph[ing]:
                indegree[rec] -= 1

                if indegree[rec] == 0:
                    cookable.append(rec)
                    queue.append(rec)

        return cookable