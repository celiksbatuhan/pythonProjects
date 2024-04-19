class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        A = []
        B = []
        for move in moves:
            if moves.index(move) % 2 == 0:
                A.append(move)
            else:
                B.append(move)
        for i in range(2):
            if i == 0:
                player = A
            else:
                player = B
            for j in range(3):
                if (
                    all(coord in player for coord in [[j, 0], [j, 1], [j, 2]])
                    or all(coord in player for coord in [[0, j], [1, j], [2, j]])
                    or all(coord in player for coord in [[0, 0], [1, 1], [2, 2]])
                    or all(coord in player for coord in [[0, 2], [1, 1], [2, 0]])
                ):
                    return "A" if player == A else "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"


solution = Solution()

moves = []
while True:
    try:
        move = list(map(int, input().split(",")))
        moves.append(move)
    except ValueError:
        break

print(solution.tictactoe(moves))
