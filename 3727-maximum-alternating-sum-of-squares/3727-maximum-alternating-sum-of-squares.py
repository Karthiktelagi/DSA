
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        half = n // 2

        small = sum(x * x for x in nums[:half])
        total = sum(x * x for x in nums)

        return total - 2 * small
