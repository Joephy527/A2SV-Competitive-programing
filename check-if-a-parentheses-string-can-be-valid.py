class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        stack = []
        unlocked = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            elif c == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while (
            stack and unlocked and
            stack[-1] < unlocked[-1]
        ):
            stack.pop()
            unlocked.pop()

        return not stack
