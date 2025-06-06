class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = [n for n in range(26)]
        smallest = []

        def find(c):
            while graph[c] != c:
                c = graph[c]

            return c

        def union(c1, c2):
            char1, char2 = find(c1), find(c2)

            if char1 > char2:
                graph[char1] = char2
            elif char2 > char1:
                graph[char2] = char1

        for c1, c2 in zip(s1, s2):
            char1, char2 = ord(c1) - ord("a"), ord(c2) - ord("a")
            union(char1, char2)

        for c in baseStr:
            char = ord(c) - ord("a")
            smallest.append(chr(find(char) + ord("a")))

        return "".join(smallest)