class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return

        count = Counter(hand)
        hands = sorted(count.keys())

        for h in hands:
            if count[h]:
                for i in range(1, groupSize):
                    if count[h + i] < count[h]:
                        return

                    count[h + i] -= count[h]

        return True
