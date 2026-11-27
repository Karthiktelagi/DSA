from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1

        # Precompute how many items have a factor divisible by f
        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples[f] += freq[m]

        # 0/1 Knapsack for first-time purchases
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for factor, price in items:
            min_price = min(min_price, price)
            gain = multiples[factor]  # 1 purchased copy + (multiples[factor] - 1) free copies
            for c in range(budget, price - 1, -1):
                if dp[c - price] + gain > dp[c]:
                    dp[c] = dp[c - price] + gain

        # Spend leftover budget greedily on the cheapest item
        ans = 0
        for c in range(budget + 1):
            extra = (budget - c) // min_price
            if dp[c] + extra > ans:
                ans = dp[c] + extra

        return ans