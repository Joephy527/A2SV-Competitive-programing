class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        min_char = 0
        stack, p = [], []

        for c in s:
            stack.append(c)
            count[c] -= 1

            while (
                min_char != ord("z") and
                not count[chr(min_char)]
            ):
                min_char += 1

            min_character = chr(min_char)

            while stack and stack[-1] <= min_character:
                p.append(stack.pop())

        return "".join(p)