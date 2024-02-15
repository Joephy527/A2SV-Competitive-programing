class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        hours = {}

        for i in range(len(speed)):
            hour = (target - position[i]) / speed[i]
            hours[position[i]] = hour

        position.sort(reverse=True)

        for p in position:
            if not fleet or fleet[-1] < hours[p]:
                fleet.append(hours[p])

        return len(fleet)
