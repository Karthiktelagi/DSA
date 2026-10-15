from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.append(0)

        for i in range(len(diff) - 1):
            count = i + 1
            cost = (diff[i] - diff[i + 1]) * count

            if k >= cost:
                k -= cost
            else:
                level = k // count
                rem = k % count

                for j in range(count):
                    diff[j] = diff[i] - level

                for j in range(rem):
                    diff[j] -= 1

                k = 0
                break

        if k > 0:
            for i in range(len(diff) - 1):
                diff[i] = 0

        return sum(d * d for d in diff[:-1])