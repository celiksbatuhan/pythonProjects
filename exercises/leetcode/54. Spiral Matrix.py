class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        final_list = []
        final_list += (matrix[0])
        for i in range(1, len(matrix)-1):
            final_list += [matrix[i][-1]]
        final_list += matrix[-1][::-1]
        for i in range(len(matrix)-2,0,-1):
            final_list += [matrix[i][0]]
        return final_list
    

solution = Solution()

print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]