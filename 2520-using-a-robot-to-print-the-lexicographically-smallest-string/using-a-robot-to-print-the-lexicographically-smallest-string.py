class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        min_char = ord("a")
        smallest, stack = [], []
    
        for c in s:
            stack.append(c)
            count[c] -= 1

            while (
                min_char < ord("z") and
                not count[chr(min_char)]
            ):
                min_char += 1

            while stack and stack[-1] <= chr(min_char):
                smallest.append(stack.pop())

        return "".join(smallest)