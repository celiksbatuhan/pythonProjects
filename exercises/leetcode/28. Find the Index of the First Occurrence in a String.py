class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


solution = Solution()

haystack = input()
needle = input()

print(solution.strStr(haystack, needle))
