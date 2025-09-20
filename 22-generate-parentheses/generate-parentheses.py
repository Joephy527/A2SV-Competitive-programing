class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        parentheses = []
        
        def back_track(op = 0, closed = 0):
            if closed == n:
                parentheses.append("".join(combination))

                return

            if op < n:
                combination.append("(")
                back_track(op + 1, closed)
                combination.pop()

            if closed < op:
                combination.append(")")
                back_track(op, closed + 1)
                combination.pop()

        back_track()

        return parentheses