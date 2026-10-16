
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        sum1 = [0] * size
        sum2 = [0] * size
        lazy = [0] * size

        def apply(node, length, val):
            sum2[node] = (
                sum2[node] + 2 * val * sum1[node]
                + length * val * val
            ) % MOD
            sum1[node] = (sum1[node] + length * val) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2
            val = lazy[node]

            apply(node * 2, mid - start + 1, val)
            apply(node * 2 + 1, end - mid, val)

            lazy[node] = 0

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                apply(node, end - start + 1, 1)
                return

            push(node, start, end)
            mid = (start + end) // 2

            if left <= mid:
                update(node * 2, start, mid, left, right)

            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD

            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + sum2[1]) % MOD

        return ans
