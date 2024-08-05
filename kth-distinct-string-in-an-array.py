class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        for char in arr:
            if count[char] == 1:
                k -= 1

            if not k:
                return char

        return ""
