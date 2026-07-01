class Solution:
    def isValid(self, s: str) -> bool:
        characters = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for parentheses in s:
            if parentheses in characters:
                stack.append(parentheses)

                continue

            if not stack or parentheses != characters[stack.pop()]:
                return False

        return not stack