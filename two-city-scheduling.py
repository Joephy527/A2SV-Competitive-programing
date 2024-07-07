class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        cost = cityA = cityB = 0

        for costA, costB in costs:
            if (cityB == len(costs) // 2 or
                (costA <= costB and cityA < len(costs) // 2)):
                cost += costA
                cityA += 1
            else:
                cost += costB
                cityB += 1

        return cost
