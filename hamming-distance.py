class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binaries = [int(binary) for binary in bin(x ^ y)[2:]]
        distance = 0

        for binary in binaries:
            distance += binary
        
        return distance
