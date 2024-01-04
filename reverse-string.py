class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(string, l, r):
            if l >= r: return

            string[l], string[r] = string[r], string[l]

            return swap(string, l + 1, r - 1)

        swap(s, 0, len(s) - 1)
