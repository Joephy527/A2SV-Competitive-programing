class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)
        stack = []
        
        def part_exists(n, p1):
            p2 = 0

            while p1 < n and p2 < k:
                if stack[p1] != part[p2]:
                    return

                p1 += 1
                p2 += 1

            return p2 == k

        for c in s:
            stack.append(c)
            n = len(stack)

            if (
                c == part[-1] and
                n >= k and
                part_exists(n, n - k)
            ):
                for _ in range(k):
                    stack.pop()

        return "".join(stack)
