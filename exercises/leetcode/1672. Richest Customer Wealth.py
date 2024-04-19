class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealths = [sum(account) for account in accounts]
        return max(wealths)


solution = Solution()

accounts = []
while True:
    try:
        account = list(map(int, input().split(",")))
        accounts.append(account)
    except ValueError:
        break

print(solution.maximumWealth(accounts))
