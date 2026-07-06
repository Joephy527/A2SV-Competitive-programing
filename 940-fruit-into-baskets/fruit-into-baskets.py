class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        p = max_fruits = 0

        for s in range(len(fruits)):
            count[fruits[s]] += 1

            while len(count) > 2:
                count[fruits[p]] -= 1
                
                if count[fruits[p]] == 0:
                    del count[fruits[p]]

                p += 1

            max_fruits = max(
                max_fruits,
                s - p + 1
            )

        return max_fruits