class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                sub_string = s[:length]
                if sub_string * (n // length) == s:
                    return True
        return False


solution = Solution()

s = input()

print(solution.repeatedSubstringPattern(s))
