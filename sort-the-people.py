class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def select(index):
            idx = index
            for j in range(i + 1, len(names)):
                if heights[idx] < heights[j]:
                    idx = j

            return idx
        
        for i in range(len(names) - 1):
            idx = select(i)

            heights[i], heights[idx] = heights[idx], heights[i]
            names[i], names[idx] = names[idx], names[i]

        return names
