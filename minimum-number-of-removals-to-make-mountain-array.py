class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        minRemoval = float("inf")

        increasingSeq = self.getLongestSubsequenceLengths(nums)
        nums.reverse()
        
        decreasingSeq = self.getLongestSubsequenceLengths(nums)
        decreasingSeq.reverse()

        for i in range(n):
            if increasingSeq[i] > 1 and decreasingSeq[i] > 1:
                minRemoval = min(
                    minRemoval, n - increasingSeq[i] - decreasingSeq[i] + 1
                )

        return minRemoval

    def getLongestSubsequenceLengths(self, nums: List[int]) -> List[int]:
        maxSequence = [1] * len(nums)
        sequence = [nums[0]]

        for i in range(1, len(nums)):
            index = self.lowerBound(sequence, nums[i])

            if index == len(sequence):
                sequence.append(nums[i])
            else:
                sequence[index] = nums[i]

            maxSequence[i] = len(sequence)

        return maxSequence

    def lowerBound(self, sequence: List[int], target: int) -> int:
        left, right = 0, len(sequence)
        
        while left < right:
            mid = left + (right - left) // 2
        
            if sequence[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
