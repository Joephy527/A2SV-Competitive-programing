class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        currentCapacity = capacity
        steps = 0

        for i in range(len(plants) - 1):
            steps += 1
            currentCapacity -= plants[i]

            if plants[i + 1] > currentCapacity:
                steps += (2 * i) + 2
                currentCapacity = capacity

        return steps + 1
