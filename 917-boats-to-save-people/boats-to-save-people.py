class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = boats = 0
        right = len(people) - 1

        people.sort()

        while left < right:
            weight = people[left] + people[right]
            
            if weight <= limit:
                left += 1
            
            right -= 1
            boats += 1

        boats += left == right

        return boats