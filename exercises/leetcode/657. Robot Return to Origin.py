class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movement = [0, 0]
        for move in moves:
            match move:
                case "U":
                    movement[1] += 1
                case "D":
                    movement[1] -= 1
                case "L":
                    movement[0] -= 1
                case "R":
                    movement[0] += 1
        if movement == [0, 0]:
            return True
        else:
            return False


solution = Solution()

moves = input()

print(solution.judgeCircle(moves))
