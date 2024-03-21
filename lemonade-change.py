class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        profit = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                profit[5] += 1
            elif bill == 10:
                if not profit[5]:
                    return False

                profit[10] +=1
                profit[5] -= 1
            else:
                if profit[5] and profit[10]:
                    profit[5] -= 1
                    profit[10] -=1
                elif profit[5] >= 3: 
                    profit[5] -= 3
                else:
                    return False

        return True
