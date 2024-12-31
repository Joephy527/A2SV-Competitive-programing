class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        gas_total = start_station = 0

        for i in range(len(gas)):
            gas_total += gas[i] - cost[i]

            if gas_total < 0:
                start_station = i + 1
                gas_total = 0

        return start_station
