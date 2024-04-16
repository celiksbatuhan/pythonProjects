class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        for index, num in enumerate(nums):
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums


solution = Solution()

nums = list(map(int, input().split()))

print(solution.moveZeroes(nums))
