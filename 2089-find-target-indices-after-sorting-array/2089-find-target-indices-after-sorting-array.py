
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = sum(x < target for x in nums)
        equal = nums.count(target)

        return list(range(smaller, smaller + equal))
