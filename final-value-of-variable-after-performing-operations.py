class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        operationsMap = {
            "--X": lambda x: x - 1,
            "X--": lambda x: x - 1,
            "X++": lambda x: x + 1,
            "++X": lambda x: x + 1
        }

        for operation in operations:
            x = operationsMap[operation](x)

        return x
