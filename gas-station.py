class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        n = len(gas)
        gasSum = idx = 0

        for i in range(n):
            gasSum += (gas[i] - cost[i])

            if gasSum < 0 and i < n - 1:
                idx = i + 1
                gasSum = 0

        return idx
