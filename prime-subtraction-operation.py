class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maxVal, minVal, idx = max(nums), 1, 0
        primes = [True] * (maxVal + 1)
        primes[1] = False

        for num in range(2, int((maxVal + 1) ** 0.5) + 1):
            if primes[num]:
                for multiple in range(num * num, maxVal + 1, num):
                    primes[multiple] = False

        while idx < len(nums):
            dif = nums[idx] - minVal

            if dif < 0:
                return False

            if primes[dif]:
                idx += 1
            
            minVal += 1

        return True
