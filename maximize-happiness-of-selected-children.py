class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        decriment = maxHappiness = 0

        for num in happiness:
            if k > 0: 
                hap = num - decriment
                maxHappiness += hap if hap > 0 else 0
                decriment += 1
                k -= 1
            else:
                break

        return maxHappiness
