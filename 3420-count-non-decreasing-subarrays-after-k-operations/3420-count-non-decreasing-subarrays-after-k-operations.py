
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()

        cost = 0
        ans = 0
        j = n - 1

        for i in range(n - 1, -1, -1):

            # Maintain monotonic deque
            while dq and nums[dq[-1]] < nums[i]:
                l = dq.pop()

                r = j + 1 if not dq else dq[-1]

                cost += (r - l) * (nums[i] - nums[l])

            dq.append(i)

            # Shrink window if cost exceeds k
            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            # Count valid subarrays
            ans += j - i + 1

        return ans
