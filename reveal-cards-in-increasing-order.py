class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        res = [0] * len(deck)

        for card in deck:
            idx = queue.popleft()
            res[idx] = card

            if queue:
                queue.append(queue.popleft())
            
        return res
