class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        positions = []
        
        for f in factory:
            positions.extend([f[0]] * f[1])
        
        robotCount = len(robot)
        factoryCount = len(positions)

        memo = [[None] * (factoryCount + 1) for _ in range(robotCount + 1)]

        def findMinDistance(robotIdx: int, factoryIdx: int) -> int:
            if memo[robotIdx][factoryIdx] is not None:
                return memo[robotIdx][factoryIdx]
            
            if robotIdx == robotCount:
                memo[robotIdx][factoryIdx] = 0
                return 0
            
            if factoryIdx == factoryCount:
                memo[robotIdx][factoryIdx] = int(1e12)
                return int(1e12)

            repared = abs(
                robot[robotIdx] - positions[factoryIdx]
            ) + findMinDistance(robotIdx + 1, factoryIdx + 1)

            skipped = findMinDistance(robotIdx, factoryIdx + 1)

            minDistance = min(repared, skipped)
            memo[robotIdx][factoryIdx] = minDistance
            
            return minDistance

        return findMinDistance(0, 0)
