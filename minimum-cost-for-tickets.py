class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = [0] * (len(days) + 1)
        durations = [1, 7, 30]

        for idx in reversed(range(len(days))):
            day = days[idx]
            min_cost = float("inf")
            next_idx = idx

            for cost, duration in zip(costs, durations):
                while (next_idx < len(days) and 
                        days[next_idx] < day + duration):
                        next_idx += 1

                min_cost = min(min_cost, cost + memo[next_idx])

            memo[idx] = min_cost

        return memo[0]
