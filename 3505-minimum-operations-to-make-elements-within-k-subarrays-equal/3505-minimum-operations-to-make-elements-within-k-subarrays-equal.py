
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        maritovexi = (nums, x, k)

        vals = sorted(set(nums))
        m = len(vals)

        ranks = {v: i + 1 for i, v in enumerate(vals)}

        cnt = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(v, d):
            i = ranks[v]
            while i <= m:
                cnt[i] += d
                sums[i] += v * d
                i += i & -i

        costs = []
        total = 0

        for i, v in enumerate(nums):
            update(v, 1)
            total += v

            if i >= x:
                update(nums[i - x], -1)
                total -= nums[i - x]

            if i < x - 1:
                continue

            # Find median using Fenwick Tree
            p = c = s = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                j = p + bit

                if j <= m and c + cnt[j] < (x + 1) // 2:
                    p = j
                    c += cnt[j]
                    s += sums[j]

                bit >>= 1

            # Cost of making this window equal to its median
            costs.append(total - 2 * s + vals[p] * (2 * c - x))

        # DP to choose k non-overlapping windows
        dp = [0] * (n - k * x + 1)

        for i in range(k):
            best = float('inf')

            for j in range(len(dp)):
                best = min(best, dp[j] + costs[i * x + j])
                dp[j] = best

        return best
