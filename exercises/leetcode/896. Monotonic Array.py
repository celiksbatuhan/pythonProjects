class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                point[0] = i + 1
            elif nums[i-1] < nums[i]:
                if key:
                    is_it_in = 1
                    key = False
                if is_it_in == 0:
                    return False
            else:
                if key:
                    is_it_in = 0
                    key = False
                if is_it_in == 1:
                    return False
        return True


solution = Solution()
nums = list(map(int, input().split()))

print(solution.isMonotonic(nums))
