class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        initial = strs[0]
        prefix = len(initial)

        def get_prefix_idx(string):
            p = 0

            while (
                p < len(string) and
                p < prefix and
                string[p] == initial[p]
            ):
                p += 1

            return p

        for string in strs:
            prefix = get_prefix_idx(string)

        return initial[:prefix]