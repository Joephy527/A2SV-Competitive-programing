class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def back_track():
            sequences_count.add("".join(sequence))

            for pos, char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    sequence.append(char)

                    back_track()

                    sequence.pop()
                    used[pos] = False
        
        sequences_count = set()
        sequence = []
        used = [False] * len(tiles)

        back_track()

        return len(sequences_count) - 1
