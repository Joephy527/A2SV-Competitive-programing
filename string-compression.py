class Solution:
    def compress(self, chars: List[str]) -> int:
        p = 0
        keepTrack = 0

        for s in range(1, len(chars)):
            if chars[s] != chars[p]:
                char = chars[p]
                count = str(s - p)
                
                if count > "1":
                    char += count

                for i in char:
                    chars[keepTrack] = i
                    keepTrack += 1

                p = s

            if s == len(chars) - 1 and chars[s] == chars[p]:
                count = str(s - p + 1)
                char = chars[p]

                if count > "1":
                    char += count

                for i in char:
                    chars[keepTrack] = i
                    keepTrack += 1

        return 1 if keepTrack == 0 else keepTrack
