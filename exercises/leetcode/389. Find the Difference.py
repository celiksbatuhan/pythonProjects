from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s, count_t = Counter(s), Counter(t)
        for i in count_t:
            if i not in count_s:
                return i
            if count_s[i] < count_t[i]:
                return i


solution = Solution()

s = input()
t = input()

print(solution.findTheDifference(s, t))
