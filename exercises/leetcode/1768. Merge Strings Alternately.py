class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        for i in range(min_len):
            merged += word1[i] + word2[i]
        merged += word1[min_len:]
        merged += word2[min_len:]
        return merged


solution = Solution()

word1 = input()
word2 = input()

print(solution.mergeAlternately(word1, word2))
