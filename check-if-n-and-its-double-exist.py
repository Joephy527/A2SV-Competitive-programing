class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        def isSeenBefore(num):
            return 2 * num in seen or num / 2 in seen

        for num in arr:
            if isSeenBefore(num):
                return True

            seen.add(num)

        return False
