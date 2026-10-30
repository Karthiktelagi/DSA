
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # Prefix maximum and suffix minimum
        pref_max = [0] * (n + 1)
        suff_min = [float('inf')] * (n + 1)

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        # Count adjacent descents
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i])

        # Check every divisor k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                end = start + k - 1

                # Count descents inside the block
                count = drops[end] - drops[start]

                # Include circular boundary
                if nums[end] > nums[start]:
                    count += 1

                if count > 1:
                    valid = False
                    break

                # Ensure this block can follow the previous blocks
                if start > 0 and pref_max[start] > suff_min[start]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
