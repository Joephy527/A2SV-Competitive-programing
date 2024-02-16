class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        parentheses = []

        def backTrack(openCount, closedCount):
            if openCount == closedCount == n:
                combinations.append("".join(parentheses))

                return

            if openCount < n:
                parentheses.append("(")
                backTrack(openCount + 1, closedCount)
                parentheses.pop()

            if closedCount < openCount:
                parentheses.append(")")
                backTrack(openCount, closedCount + 1)
                parentheses.pop()

        backTrack(0, 0)

        return combinations
