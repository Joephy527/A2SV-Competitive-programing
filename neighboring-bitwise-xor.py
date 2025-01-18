class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0

        for bit in derived:
            xor ^= bit

        return not xor
