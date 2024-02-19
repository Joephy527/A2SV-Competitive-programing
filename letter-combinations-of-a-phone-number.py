class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephoneButtons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combinations = []

        def backTrack(idx, curStr):
            if len(curStr) >= len(digits):
                combinations.append(curStr)

                return

            for char in telephoneButtons[digits[idx]]:
                backTrack(idx + 1, curStr + char)

        if digits:
            backTrack(0, "")

        return combinations
