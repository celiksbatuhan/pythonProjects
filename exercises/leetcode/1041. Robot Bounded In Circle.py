class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in instructions:
            if i == "G":
                x += movements[direction][0]
                y += movements[direction][1]
            elif i == "L":
                direction = (direction - 1) % 4
            elif i == "R":
                direction = (direction + 1) % 4
        return (x == 0 and y == 0) or direction != 0


solution = Solution()

instructions = input()

print(solution.isRobotBounded(instructions))
