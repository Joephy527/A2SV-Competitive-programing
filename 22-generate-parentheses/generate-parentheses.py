class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        parentheses = []

        def back_track(opened = 0, closed = 0):
            if opened == closed == n:
                combinations.append("".join(parentheses))

                return

            if opened < n:
                parentheses.append("(")
                back_track(opened + 1, closed)
                parentheses.pop()

            if opened > closed:
                parentheses.append(")")
                back_track(opened, closed + 1)
                parentheses.pop()

        back_track()

        return combinations