class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        if len(mat) == len(mat[0]):
            diag_sum = 0
            for i in range(len(mat)):
                for j in range(len(mat)):
                    if i == j or i + j == len(mat) - 1:
                        diag_sum += mat[i][j]
            return diag_sum
        else:
            return 123456789
        

solution = Solution()

mat = []
while True:
    try:
        row = list(map(int, input().split(",")))
        mat.append(row)
    except ValueError:
        break

print(solution.diagonalSum(mat))