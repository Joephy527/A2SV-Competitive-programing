class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        combination = []

        def back_track(idx = 1):
            if len(combination) == k:
                combinations.append(combination[:])

                return

            for num in range(idx, n + 1):
                combination.append(num)
                back_track(num + 1)
                combination.pop()

        back_track()

        return combinations