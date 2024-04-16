from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc, tc = Counter(s), Counter(t)
        if len(s) == len(t):
            for i in sc:
                if i in tc and tc[i] == sc[i]:
                    continue
                else:
                    return False
            return True
        else:
            return False


solution = Solution()

s = input()
t = input()

print(solution.isAnagram(s, t))
