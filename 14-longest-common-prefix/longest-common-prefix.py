class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        initial = strs[0]

        def get_prefix_idx(string):
            p = 0

            while (
                p < len(string) and
                p < prefix and
                string[p] == initial[p]
            ):
                p += 1

            return p

        prefix = len(strs[0])

        for idx in range(1, n):
            prefix = get_prefix_idx(strs[idx])

        return strs[0][:prefix]