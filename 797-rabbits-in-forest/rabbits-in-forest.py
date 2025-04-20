class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabbits = 0

        for color, cnt in count.items():
            group_size = color + 1
            group = ceil(cnt / group_size)
            rabbits += group * group_size

        return rabbits