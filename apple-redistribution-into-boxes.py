class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApple = sum(apple)
        capacity.sort(reverse=True)
        totalCapacity = 0

        for idx, num in enumerate(capacity):
            totalCapacity += num
            
            if totalCapacity >= totalApple:
                return idx + 1
