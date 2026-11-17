
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes for every substring
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                best = INF

                # Find all proper divisors
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check palindrome groups
                    for i in range(d):
                        left = l + i
                        right = l + i + ((length - 1 - i) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[l][r] = best

        # Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i // 2) + 1):
                for p in range(2 * (j - 1), i - 1):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[p][j - 1] + cost[p][i - 1]
                    )

        return dp[n][k]
