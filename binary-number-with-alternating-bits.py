class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binaries = [int(binary) for binary in bin(n)[2:]]

        for i in range(1, len(binaries)):
            if binaries[i] == binaries[i - 1]:
                return
        
        return True
