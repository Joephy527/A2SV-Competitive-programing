class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_one = -1
        distance = 0

        for idx, seat in enumerate(seats):
            if seat:
                if last_one == -1:
                    distance = idx
                else:
                    distance = max(
                        distance,
                        (idx - last_one) // 2
                    )

                last_one = idx

        return max(
            distance,
            len(seats) - last_one - 1
        )