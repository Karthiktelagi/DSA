
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {num: i for i, num in enumerate(sorted_nums)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
