class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        sorted_arr = sorted(arr)
        pattern = sorted_arr[0] - sorted_arr[1]
        for i in range(1, len(arr)):
            if sorted_arr[i - 1] - sorted_arr[i] != pattern:
                return False
        return True


solution = Solution()

arr = list(map(int, input().split()))

print(solution.canMakeArithmeticProgression(arr))
