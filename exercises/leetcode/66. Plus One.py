class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join(map(str, digits)))
        number += 1
        return [int(digit) for digit in str(number)]


solution = Solution()

digits = list(map(int, input().split()))

print(solution.plusOne(digits))
